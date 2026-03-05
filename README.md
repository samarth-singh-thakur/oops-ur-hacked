# 👻 GHOSTWATCHER - Mr. Robot Inspired Webcam Capture

A cyberpunk-themed web application inspired by the TV series **Mr. Robot** that captures photos from your webcam with stunning hacker aesthetics and viral-worthy animations.

![GHOSTWATCHER](https://img.shields.io/badge/Status-ACTIVE-00ff41?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi)

## 🎯 Features

### 🎨 Visual Effects
- **Matrix Rain Background** - Animated falling characters in the background
- **CRT Scanline Effect** - Retro monitor scanlines overlay
- **Glitch Animations** - Random screen glitches for authentic hacker feel
- **Neon Glow Effects** - Green terminal-style glowing text and borders
- **Loading Animations** - Cool progress bars and status messages
- **Blinking "CAPTURED" Badge** - Red alert badge on captured images

### 💻 Technical Features
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Real-time Webcam Capture** - Instant photo capture via backend API
- **Smooth Animations** - CSS3 animations for professional feel
- **Terminal-Style UI** - Command-line interface aesthetic
- **Auto-cleanup** - Photos are automatically deleted after streaming
- **Network Accessible** - Access from any device on your local network

### 🎮 User Experience
- **One-Click Capture** - Simple button to capture photos
- **Keyboard Shortcut** - Press `Ctrl/Cmd + Enter` to capture
- **Status Messages** - Real-time feedback on capture progress
- **Sound Effects** - Optional audio feedback on successful capture
- **Image Preview** - Captured photos display with cool animations

## 🚀 Quick Start

### Prerequisites
```bash
# Install required packages
pip install fastapi uvicorn opencv-python
```

### Running the Server
```bash
# Start the server
python3 run_server.py
```

The server will start and display:
```
============================================================
🚀 Starting FastAPI Server
============================================================
Local access:   http://127.0.0.1:8000
Network access: http://192.168.1.x:8000
============================================================

Endpoints:
  - http://192.168.1.x:8000/ (main webpage)
  - http://192.168.1.x:8000/ghostwatcher (capture photo API)
  - http://192.168.1.x:8000/health (health check)
  - http://192.168.1.x:8000/docs (API documentation)
============================================================
```

### Access the Application
1. Open your browser
2. Navigate to `http://127.0.0.1:8000` (local) or `http://YOUR_IP:8000` (network)
3. Click **"INITIATE CAPTURE"** button
4. Watch the cool animations as your photo is captured!

## 📱 Responsive Design

### Desktop (1200px+)
- Full-width layout with large terminal windows
- Prominent button and title
- Maximum visual impact

### Tablet (768px - 1199px)
- Optimized spacing and font sizes
- Maintains all visual effects
- Touch-friendly interface

### Mobile (< 768px)
- Stacked vertical layout
- Scaled-down text for readability
- Optimized button sizes for touch
- Maintains all animations

## 🎨 Design Inspiration

The design is heavily inspired by the TV series **Mr. Robot**, featuring:
- **Color Scheme**: Black background with neon green (#00ff41) and red (#ff0066) accents
- **Typography**: Monospace fonts (Courier New) for terminal aesthetic
- **Visual Style**: Hacker/cyberpunk theme with glitch effects
- **UI Elements**: Terminal-style command prompts and status messages

## 🛠️ Technical Stack

### Backend
- **FastAPI** - Modern Python web framework
- **OpenCV** - Webcam capture and image processing
- **Uvicorn** - ASGI server

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Advanced animations and effects
- **Vanilla JavaScript** - No dependencies, pure JS
- **Canvas API** - Matrix rain effect

## 📂 Project Structure

```
oops-ur-hacked/
├── index.html           # Main webpage with Mr. Robot theme
├── server.py            # FastAPI server with endpoints
├── run_server.py        # Server startup script
├── webcam_capture.py    # Webcam capture logic
├── captured_photos/     # Temporary photo storage (auto-cleanup)
└── README.md           # This file
```

## 🔧 API Endpoints

### `GET /`
Returns the main HTML page with the GHOSTWATCHER interface.

### `GET /ghostwatcher`
Captures a photo from the webcam and returns it as a streaming response.
- **Response**: Image (JPEG)
- **Headers**: `Cache-Control: no-store`
- **Behavior**: Photo is deleted after streaming

### `GET /health`
Health check endpoint.
- **Response**: `{"ok": true}`

### `GET /docs`
Interactive API documentation (Swagger UI).

## 🎯 Use Cases

- **Security Monitoring** - Capture photos when motion is detected
- **Fun Photo Booth** - Create a cyberpunk-themed photo booth
- **Pranks** - Surprise visitors with the hacker aesthetic
- **Learning Project** - Study web development and computer vision
- **Social Media Content** - Create viral-worthy content with the unique design

## ⚙️ Configuration

### Change Port
Edit `run_server.py`:
```python
port = 8000  # Change to your desired port
```

### Camera Settings
Edit `webcam_capture.py`:
```python
camera_index = 0      # Change camera (0 = default, 1 = external)
warmup_frames = 10    # Adjust camera warmup time
```

## 🔒 Security Notes

- The server binds to `0.0.0.0` to accept network connections
- Photos are automatically deleted after streaming
- No persistent storage of captured images
- Use in trusted networks only

## 🎬 Demo

1. **Initial State**: Terminal-style interface with glowing green text
2. **Click Button**: Loading animation with progress bar
3. **Capture**: Status messages update in real-time
4. **Display**: Photo appears with glowing border and "CAPTURED" badge
5. **Effects**: Scanlines, glitch effects, and matrix rain throughout

## 🤝 Contributing

Feel free to fork this project and add your own features:
- Additional visual effects
- More camera controls
- Photo filters
- Multi-camera support
- Photo gallery
- Social media sharing

## 📝 License

This project is open source and available for educational purposes.

## 🎉 Credits

- Inspired by **Mr. Robot** TV series
- Built with ❤️ and lots of caffeine ☕
- Matrix rain effect inspired by The Matrix

## 🐛 Troubleshooting

### Camera Not Working
```bash
# Check camera permissions
# macOS: System Preferences > Security & Privacy > Camera
# Linux: Check /dev/video0 permissions
```

### Port Already in Use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Module Not Found
```bash
# Install dependencies
pip install fastapi uvicorn opencv-python
```

---

**Made with 💚 by a Mr. Robot fan**

*"Hello, friend. Welcome to GHOSTWATCHER."*