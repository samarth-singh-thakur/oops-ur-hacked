#!/usr/bin/env python3
"""
Startup script to run the FastAPI server accessible on local network.
"""
import socket
import subprocess
import sys


def get_local_ip():
    """Get the local IP address of this machine."""
    try:
        # Create a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external address (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "Unable to determine"


def main():
    """Run the uvicorn server with network access."""
    local_ip = get_local_ip()
    port = 8000
    
    print("=" * 60)
    print("🚀 Starting FastAPI Server")
    print("=" * 60)
    print(f"Local access:   http://127.0.0.1:{port}")
    print(f"Network access: http://{local_ip}:{port}")
    print("=" * 60)
    print("\nEndpoints:")
    print(f"  - http://{local_ip}:{port}/ghostwatcher (capture photo)")
    print(f"  - http://{local_ip}:{port}/health (health check)")
    print(f"  - http://{local_ip}:{port}/docs (API documentation)")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    print()
    
    # Run uvicorn with host 0.0.0.0 to accept connections from any network interface
    try:
        subprocess.run([
            "uvicorn",
            "server:app",
            "--host", "0.0.0.0",
            "--port", str(port)
        ])
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")
        sys.exit(0)


if __name__ == "__main__":
    main()

# Made with Bob
