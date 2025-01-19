# DHT22 Sensor with Raspberry Pi for Environmental Monitoring

This project demonstrates how to use a DHT22 sensor with a Raspberry Pi to monitor and log environmental data such as temperature and humidity. Designed for simplicity, it provides an easy-to-follow setup suitable for household use.

---

## Features
- **Simple Setup**: Connect a DHT22 sensor to your Raspberry Pi with minimal hardware.
- **Real-time Monitoring**: Read temperature and humidity data in real-time.
- **Data Logging**: Save environmental data for future analysis.
- **Web Preview**: View logged data in your browser using a Flask-based web application.
- **Python-based**: Built using Python for ease of use and customization.

---

## Prerequisites

### Hardware
- Raspberry Pi (any model with GPIO pins)
- DHT22 sensor
- Jumper wires

### Software
- Raspberry Pi OS (or a compatible Linux distribution)
- Python 3.x
- `Adafruit_DHT` library
- `Flask` library

---

## Installation

### 1. Set Up the Raspberry Pi
Ensure your Raspberry Pi is powered on and connected to the internet. Update the system:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Clone the Repository
```bash
git clone https://github.com/plerixus/temp_sensor.git
cd temp_sensor
```

### 3. Install Required Libraries
Install the necessary Python libraries:
```bash
pip install Adafruit_DHT Flask
```

---

## Wiring the DHT22 Sensor

1. Connect the DHT22 sensor's pins to the Raspberry Pi GPIO as follows:
   - **VCC**: 3.3V pin on the Raspberry Pi
   - **GND**: Ground pin on the Raspberry Pi
   - **DATA**: Any GPIO pin (e.g., GPIO4)


---

## Usage

### 1. Update the Configuration
Modify the GPIO pin in the script (default is GPIO4):
```python
DHT_PIN = 4  # Update this to the GPIO pin used for the sensor
```

### 2. Run the Logger Script
Execute the script to start monitoring:
```bash
python dht22_logger.py
```

### 3. Run the Flask Application
Start the Flask application to preview the data in your browser:
```bash
python app.py
```

### 4. Access the Web Interface
Open your browser and go to:
```
http://<raspberry_pi_ip>:5000
```
Replace `<raspberry_pi_ip>` with your Raspberry Pi's IP address.

---


## Web Interface
The Flask application displays the latest temperature and humidity readings in a user-friendly format.

---

## Customization

- **Data Interval**: Adjust the data collection interval by modifying the `time.sleep()` parameter in the logger script.
- **File Format**: Change the log file format from CSV to JSON or other formats as needed.
- **Web Interface**: Customize the Flask application to add charts or additional features.

---

## Troubleshooting

### Common Issues
1. **Sensor Not Detected**: Double-check the wiring and GPIO pin configuration.
2. **Data Read Errors**: Ensure the sensor is not faulty

### Debugging
Run the script with verbose logging enabled to identify issues.


---

## Acknowledgments
Special thanks to the [Adafruit](https://github.com/adafruit) community for their excellent libraries and tutorials.

---

## Author
Created by [Plerixus](https://github.com/plerixus).
