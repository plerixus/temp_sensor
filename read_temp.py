import time
import board
import adafruit_dht
from datetime import datetime

sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity
        cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Time={0} Temp={1:0.1f}ºC, Humidity={2:0.1f}%".format(cur_time, temperature_c, humidity))

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)
