from __future__ import annotations

import mimetypes
import os
from pathlib import Path
from typing import Iterator

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from webcam_capture import capture_photo
app = FastAPI()


@app.get("/")
def read_root():
    """Serve the main HTML page"""
    return FileResponse("index.html")


def get_image_path() -> str:
    return capture_photo(save_to_folder="captured_photos")


def _media_type_for(path: Path) -> str:
    mt, _ = mimetypes.guess_type(str(path))
    return mt or "image/jpeg"


@app.get("/ghostwatcher")
def seeendpoint():
    path = Path(get_image_path())

    if not path.is_file():
        raise HTTPException(status_code=404, detail=f"Image not found: {path}")

    media_type = _media_type_for(path)
    if not media_type.startswith("image/"):
        raise HTTPException(status_code=415, detail=f"Not an image: {path.name}")

    def iter_file_then_delete() -> Iterator[bytes]:
        try:
            with open(path, "rb") as f:
                while True:
                    chunk = f.read(256 * 1024)  # 256KB
                    if not chunk:
                        break
                    yield chunk
        finally:
            # delete after streaming finishes (or client disconnect)
            try:
                os.remove(path)
            except FileNotFoundError:
                pass
            except PermissionError:
                # if some process still holds the file handle
                pass

    return StreamingResponse(
        iter_file_then_delete(),
        media_type=media_type,
        headers={"Cache-Control": "no-store"},
    )


@app.get("/health")
def health():
    return {"ok": True}