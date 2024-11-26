import time
import adafruit_dht
import board

DHT_PIN = board.D4

dht_device = adafruit_dht.DHT22(DHT_PIN)

print("START")

try:
    while True:
        try:
            temp = dht_device.temperature
            humi = dht_device.humidity

            if temp is not None and humidity is not None:
                print(f"temp : {temp:.1f}C and humi: {humi:.1f}%")
            else:
                print("Data cannot be read.")
        except RuntimeError as error:
            print(f"ERROR: {error.args[0]}")

        time.sleep(3)  # n초 간격으로 데이터 받음

except KeyboardInterrupt:
    print("End measurement")
    dht_device.exit()
