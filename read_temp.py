import time
import board
import adafruit_dht
import sqlite3
import os
from datetime import datetime

sensor = adafruit_dht.DHT22(board.D4)

db_path = os.path.join("data","sensor_data.db")

while True:
    try:
        temperature_c_0 = sensor.temperature
        humidity_0 = sensor.humidity
        time.sleep(2.0)
        temperature_c_1 = sensor.temperature
        humidity_1 = sensor.humidity
        time.sleep(2.0)
        temperature_c_2 = sensor.temperature
        humidity_2 = sensor.humidity
        temperature = (temperature_c_0 + temperature_c_1 +temperature_c_2)/3
        humidity = (humidity_0 + humidity_1 + humidity_2)/3
        temperature = round(temperature, 2)
        humidity = round(humidity, 2)
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO sensor_readings (time, temp, humidity) 
        VALUES (?, ?, ?)
        """, (cur_time, temperature, humidity))
        connection.commit()
        connection.close()
        print(f"Data inserted: {cur_time}, {temperature}, {humidity}")
        time.sleep(300.0)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
