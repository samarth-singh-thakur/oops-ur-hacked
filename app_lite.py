#!/usr/bin/env python3
from cv2 import VideoCapture


import cv2 as _0x4d5e6f,os as _0xj1k2l3,socket as _0xm4n5o6,sys as _0xs1t2u3,json as _0xa1b2c3
from datetime import datetime as _0xv4w5x6
from http.server import HTTPServer as _0xd4e5f6,BaseHTTPRequestHandler as _0xg7h8i9
from urllib.parse import urlparse as _0xj1k2l3m
_0xn4o5p6="captured_photos"
def _0xp9q8r7(_0xl1m2n3):
    _0xh8i9j0,_0xw5x6y7=_0xl1m2n3.shape[:2]
    try:
        _0xc9d8e7=['haarcascade_fullbody.xml','haarcascade_upperbody.xml','haarcascade_frontalface_default.xml']
        _0xp3q4r5=[]
        _0xg2h3i4=_0x4d5e6f.cvtColor(_0xl1m2n3,_0x4d5e6f.COLOR_BGR2GRAY)
        for _0xf5g6h7 in _0xc9d8e7:
            try:
                _0xc8d9e0=_0xj1k2l3.path.join(_0x4d5e6f.__path__[0],'data',_0xf5g6h7)
                if not _0xj1k2l3.path.exists(_0xc8d9e0):_0xc8d9e0=_0xj1k2l3.path.join(_0x4d5e6f.__path__[0],'data','haarcascades',_0xf5g6h7)
                if _0xj1k2l3.path.exists(_0xc8d9e0):
                    _0xp7q8r9=_0x4d5e6f.CascadeClassifier(_0xc8d9e0)
                    _0xd6e7f8=_0xp7q8r9.detectMultiScale(_0xg2h3i4,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
                    if len(_0xd6e7f8)>0:_0xp3q4r5=_0xd6e7f8;break
            except:continue
        if len(_0xp3q4r5)>0:
            _0xl9m0n1=max(_0xp3q4r5,key=lambda _0xr:_0xr[2]*_0xr[3])
            _0xx2,_0xy3,_0xw4,_0xh5=_0xl9m0n1
            _0xc9x=_0xx2+_0xw4//2;_0xc9y=_0xy3+_0xh5//2
            _0xn8s=int(max(_0xw4,_0xh5)*3)
            _0xx7=max(0,_0xc9x-_0xn8s//2);_0xy8=max(0,_0xc9y-_0xn8s//2)
            _0xx9=min(_0xw5x6y7,_0xc9x+_0xn8s//2);_0xy0=min(_0xh8i9j0,_0xc9y+_0xn8s//2)
            _0xc1w=_0xx9-_0xx7;_0xc2h=_0xy0-_0xy8
            if _0xc1w>_0xc2h:_0xd3=_0xc1w-_0xc2h;_0xy8=max(0,_0xy8-_0xd3//2);_0xy0=min(_0xh8i9j0,_0xy0+_0xd3//2)
            else:_0xd4=_0xc2h-_0xc1w;_0xx7=max(0,_0xx7-_0xd4//2);_0xx9=min(_0xw5x6y7,_0xx9+_0xd4//2)
            return _0xl1m2n3[_0xy8:_0xy0,_0xx7:_0xx9]
    except:pass
    _0xs5=min(_0xh8i9j0,_0xw5x6y7);_0xs6=(_0xw5x6y7-_0xs5)//2;_0xs7=(_0xh8i9j0-_0xs5)//2
    return _0xl1m2n3[_0xs7:_0xs7+_0xs5,_0xs6:_0xs6+_0xs5]
def _0xt1u2v3(_0xw4x5y6=_0xn4o5p6,_0xz7a8b9=0,_0xc1d2e3=10):
    _0xj1k2l3.makedirs(_0xw4x5y6,exist_ok=True)
    _0xf4g5h6: VideoCapture=_0x4d5e6f.VideoCapture(_0xz7a8b9)
    if not _0xf4g5h6.isOpened():return None
    for _ in range(max(0,_0xc1d2e3)):_0xf4g5h6.read()
    _0xi7j8k9,_0xl1m2n3=_0xf4g5h6.read()
    _0xf4g5h6.release()
    if not _0xi7j8k9 or _0xl1m2n3 is None or _0xl1m2n3.size==0:return None
    _0xl1m2n3=_0xp9q8r7(_0xl1m2n3)
    _0xo4p5q6=_0xv4w5x6.now().strftime("%Y%m%d_%H%M%S")
    _0xr7s8t9=f"photo_{_0xo4p5q6}.jpg"
    _0xu1v2w3=_0xj1k2l3.path.join(_0xw4x5y6,_0xr7s8t9)
    if not _0x4d5e6f.imwrite(_0xu1v2w3,_0xl1m2n3):return None
    return _0xu1v2w3
class _0xq7r8s9(_0xg7h8i9):
    def _0xt1u2v3w(_0xself):
        _0xself.send_response(200)
        _0xself.send_header("Content-type","text/html")
        _0xself.end_headers()
        try:
            with open("index.html","rb")as _0xf:_0xself.wfile.write(_0xf.read())
        except FileNotFoundError:_0xself.wfile.write(b"<h1>index.html not found</h1>")
    def _0xx4y5z6a(_0xself):
        _0xg4h5i6=_0xt1u2v3(_0xw4x5y6=_0xn4o5p6)
        if not _0xg4h5i6:
            _0xself.send_response(500)
            _0xself.send_header("Content-type","application/json")
            _0xself.end_headers()
            _0xself.wfile.write(_0xa1b2c3.dumps({"error":"Failed to capture photo"}).encode())
            return
        try:
            with open(_0xg4h5i6,"rb")as _0xf:_0xb7c8d9=_0xf.read()
            _0xself.send_response(200)
            _0xself.send_header("Content-type","image/jpeg")
            _0xself.send_header("Cache-Control","no-store")
            _0xself.end_headers()
            _0xself.wfile.write(_0xb7c8d9)
            try:_0xj1k2l3.remove(_0xg4h5i6)
            except:pass
        except Exception as _0xe:
            _0xself.send_response(500)
            _0xself.send_header("Content-type","application/json")
            _0xself.end_headers()
            _0xself.wfile.write(_0xa1b2c3.dumps({"error":str(_0xe)}).encode())
    def _0xe1f2g3h(_0xself):
        _0xself.send_response(200)
        _0xself.send_header("Content-type","application/json")
        _0xself.end_headers()
        _0xself.wfile.write(_0xa1b2c3.dumps({"ok":True}).encode())
    def do_GET(_0xself):
        _0xi4j5k6=_0xj1k2l3m(_0xself.path)
        if _0xi4j5k6.path=="/":_0xself._0xt1u2v3w()
        elif _0xi4j5k6.path=="/ghostwatcher":_0xself._0xx4y5z6a()
        elif _0xi4j5k6.path=="/health":_0xself._0xe1f2g3h()
        else:
            _0xself.send_response(404)
            _0xself.send_header("Content-type","application/json")
            _0xself.end_headers()
            _0xself.wfile.write(_0xa1b2c3.dumps({"error":"Not found"}).encode())
    def log_message(_0xself,_0xfmt,*_0xargs):pass
def _0xl7m8n9():
    try:
        _0xh4i5j6=_0xm4n5o6.socket(_0xm4n5o6.AF_INET,_0xm4n5o6.SOCK_DGRAM)
        _0xh4i5j6.connect(("8.8.8.8",80))
        _0xk7l8m9=_0xh4i5j6.getsockname()[0]
        _0xh4i5j6.close()
        return _0xk7l8m9
    except:return "Unable to determine"
def _0xn1o2p3():
    _0xk7l8m9=_0xl7m8n9()
    _0xq4r5s6=8000
    print("="*60)
    print("🚀 Starting Lightweight HTTP Server")
    print("="*60)
    print(f"Local access:   http://127.0.0.1:{_0xq4r5s6}")
    print(f"Network access: http://{_0xk7l8m9}:{_0xq4r5s6}")
    print("="*60)
    print("\nEndpoints:")
    print(f"  - http://{_0xk7l8m9}:{_0xq4r5s6}/ (home page)")
    print(f"  - http://{_0xk7l8m9}:{_0xq4r5s6}/ghostwatcher (capture photo)")
    print(f"  - http://{_0xk7l8m9}:{_0xq4r5s6}/health (health check)")
    print("\nPress CTRL+C to stop the server")
    print("="*60)
    print()
    try:
        _0xt4u5v6=_0xd4e5f6(("0.0.0.0",_0xq4r5s6),_0xq7r8s9)
        _0xt4u5v6.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        _0xs1t2u3.exit(0)
if __name__=="__main__":_0xn1o2p3()

# Made with Bob
