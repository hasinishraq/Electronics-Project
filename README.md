# 🤖 Human Following Robot

A smart autonomous robot that **follows a human target** and can be manually overridden via a real-time web dashboard. The system streams a live camera feed, displays sensor data (temperature, gas, sound), and accepts directional control commands — all from any browser on the same network.

---

## ✨ Features

- 🎯 **Human Following** — Autonomously tracks and follows a human target
- 📹 **Live Camera Feed** — Real-time video stream accessible via web dashboard
- 🕹️ **Manual Override** — Web-based directional controls (Forward / Backward / Left / Right / Stop)
- 📊 **Sensor Monitoring** — Live display of Temperature, Gas Level, and Sound readings (updated every second)
- 🌐 **Web Dashboard** — Responsive UI served directly from the robot over the local network
- 📱 **Responsive Design** — Adapts to desktop, tablet, and mobile screens

---

## 🔩 Hardware Components

| Component | Details |
|-----------|---------|
| 🖥️ **Raspberry Pi 4** | 8 GB RAM — main compute unit running the Flask server & vision pipeline |
| 📷 **Pi Camera Module** | Captures live video feed streamed to the dashboard |
| ⚙️ **DC Motors** | Drive wheels for forward, backward, left, and right movement |
| 🔌 **Motor Driver** | Controls motor speed and direction from Raspberry Pi GPIO |
| 🔋 **LiPo Battery** | Powers the entire system onboard for untethered operation |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · Flask |
| Frontend | HTML · CSS · Vanilla JavaScript |
| Communication | REST API (HTTP POST/GET) |
| Fonts | Google Fonts – Poppins |

---

## 📁 Project Structure

```
Electronics-Project/
├── backend/
│   └── server.py          # Flask server — serves frontend & handles robot commands
└── frontend/
    ├── index.html          # Dashboard UI
    ├── css/
    │   └── style.css       # Responsive styles & layout
    └── script/
        └── script.js       # Command sending & live sensor polling
```

---

## 🚀 Getting Started

### Prerequisites

- Raspberry Pi 4 (8 GB) running Raspberry Pi OS
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/hasinishraq/Electronics-Project.git
cd Electronics-Project

# 2. Install Python dependencies
pip install flask

# 3. Run the server
cd backend
python server.py
```

### Access the Dashboard

Once the server is running, open a browser on **any device on the same network** and navigate to:

```
http://<raspberry-pi-ip>:5000
```

> Find your Pi''s IP with: `hostname -I`

---

## 🎮 Dashboard Controls

The web dashboard provides a D-pad style control interface:

| Button | Action |
|--------|--------|
| **Forward** | Move robot forward |
| **Backward** | Move robot backward |
| **Left** | Turn robot left |
| **Right** | Turn robot right |
| **Stop** | Halt all movement |

---

## 🌐 API Reference

### `POST /control`

Send a movement command to the robot.

**Request Body:**
```json
{ "command": "forward" }
```

**Valid Commands:** `forward` · `backward` · `left` · `right` · `stop`

**Response:**
```json
{ "message": "Command forward executed successfully" }
```

---

### `GET /video_feed`

Returns the live MJPEG camera stream from the Pi Camera Module.

---

### `GET /sensor_data`

Returns real-time sensor readings (polled every 1 second by the frontend).

**Response:**
```json
{
  "temperature": 27.5,
  "gas": 320,
  "sound": 85
}
```

---

## 📡 Sensor Data

| Sensor | Description |
|--------|-------------|
| 🌡️ Temperature | Ambient temperature in °C |
| 💨 Gas Level | Air quality / gas concentration reading |
| 🔊 Sound | Ambient sound level |

---

## 🔧 Customization

To integrate your actual robot hardware, modify the command handler in `backend/server.py`:

```python
if command == 'forward':
    # TODO: Add your GPIO motor driver logic here
    pass
```

Similarly, update the `/sensor_data` and `/video_feed` routes to pull from your physical sensors and Pi Camera Module.

---

## 🗺️ Roadmap

- [ ] Integrate computer vision for autonomous human detection (OpenCV / YOLO)
- [ ] Add WebSocket support for lower-latency commands
- [ ] Implement obstacle avoidance
- [ ] Add authentication to the dashboard
- [ ] Log sensor data to a database for historical analysis

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/) — Lightweight Python web framework
- [Google Fonts – Poppins](https://fonts.google.com/specimen/Poppins) — Clean, modern typography
- [Raspberry Pi Foundation](https://www.raspberrypi.com/) — Single-board computer platform
