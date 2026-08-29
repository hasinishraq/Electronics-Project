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

### 🧠 Computing Units

| Component | Role |
|-----------|------|
| 🖥️ **Raspberry Pi 4** (8 GB RAM) | Main compute unit — runs Flask server, video stream & human-following logic |
| 🔵 **Arduino** | Microcontroller — handles low-level sensor reading & motor PWM signals |

### 📷 Camera

| Component | Role |
|-----------|------|
| 📷 **Raspberry Pi Camera Module** | Captures live video feed streamed to the web dashboard |

### ⚙️ Actuation

| Component | Role |
|-----------|------|
| ⚙️ **DC Motors** | Drive wheels for movement in all directions |
| 🔌 **Motor Driver** (e.g. L298N / L293D) | Controls motor speed & direction via PWM from Arduino/Pi GPIO |

### 📡 Sensors

| Sensor | Measurement | Connected To |
|--------|-------------|--------------|
| 🌡️ **DHT11 / DHT22** | Temperature & Humidity | Arduino |
| 💨 **MQ-2 / MQ-135** | Gas / Air Quality | Arduino |
| 🔊 **Sound Sensor Module** | Ambient Sound Level | Arduino |
| 📏 **HC-SR04 Ultrasonic Sensor** | Distance / Obstacle Detection | Arduino |
| 🔴 **IR Sensor Module** | Infrared human/object detection | Arduino |

### 🔋 Power

| Component | Role |
|-----------|------|
| 🔋 **LiPo Battery** | Powers the entire system onboard for untethered operation |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · Flask |
| Frontend | HTML · CSS · Vanilla JavaScript |
| Communication | REST API (HTTP POST/GET) · Serial (Arduino ↔ Raspberry Pi) |
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

## 🔗 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Raspberry Pi 4                        │
│  ┌──────────────┐    ┌────────────────────────────────┐ │
│  │  Pi Camera   │───▶│  Flask Server (server.py)      │ │
│  │  Module      │    │  - Serves web dashboard         │ │
│  └──────────────┘    │  - Streams video feed           │ │
│                      │  - Handles /control commands    │ │
│                      └──────────────┬─────────────────┘ │
└─────────────────────────────────────┼─────────────────── ┘
                                      │ USB Serial
                              ┌───────▼──────────┐
                              │    Arduino        │
                              │  - Reads sensors  │
                              │  - Drives motors  │
                              └───────┬───────────┘
                    ┌─────────────────┼──────────────────┐
                    ▼                 ▼                   ▼
             ┌──────────┐    ┌──────────────┐    ┌──────────────┐
             │  DHT11   │    │  HC-SR04     │    │ Motor Driver │
             │  MQ Gas  │    │  IR Sensor   │    │  + DC Motors │
             │  Sound   │    │  Ultrasonic  │    │              │
             └──────────┘    └──────────────┘    └──────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Raspberry Pi 4 (8 GB) running Raspberry Pi OS
- Arduino IDE (for flashing Arduino firmware)
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/hasinishraq/Electronics-Project.git
cd Electronics-Project

# 2. Install Python dependencies
pip install flask pyserial

# 3. Flash the Arduino sketch (open in Arduino IDE)
#    arduino/robot_sensors/robot_sensors.ino

# 4. Run the Flask server on Raspberry Pi
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

Returns real-time sensor readings from Arduino (polled every 1 second by the frontend).

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

| Sensor | Measurement | Description |
|--------|-------------|-------------|
| 🌡️ DHT11/DHT22 | Temperature (°C) | Ambient temperature & humidity |
| 💨 MQ-2/MQ-135 | Gas Level | Air quality / gas concentration |
| 🔊 Sound Module | Sound Level | Ambient noise detection |
| 📏 HC-SR04 | Distance (cm) | Obstacle detection & avoidance |
| 🔴 IR Sensor | Presence | Infrared human/object detection |

---

## 🔧 Customization

To integrate your hardware, modify the command handler in `backend/server.py`:

```python
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Connect to Arduino

if command == 'forward':
    ser.write(b'F')   # Send command byte to Arduino
elif command == 'backward':
    ser.write(b'B')
elif command == 'left':
    ser.write(b'L')
elif command == 'right':
    ser.write(b'R')
elif command == 'stop':
    ser.write(b'S')
```

---

## 🗺️ Roadmap

- [ ] Integrate computer vision for autonomous human detection (OpenCV / YOLO)
- [ ] Add WebSocket support for lower-latency commands
- [ ] Implement ultrasonic-based obstacle avoidance
- [ ] Add authentication to the dashboard
- [ ] Log sensor data to a database for historical analysis
- [ ] Add GPS module for outdoor tracking

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/) — Lightweight Python web framework
- [Google Fonts – Poppins](https://fonts.google.com/specimen/Poppins) — Clean, modern typography
- [Raspberry Pi Foundation](https://www.raspberrypi.com/) — Single-board computer platform
- [Arduino](https://www.arduino.cc/) — Open-source microcontroller platform
