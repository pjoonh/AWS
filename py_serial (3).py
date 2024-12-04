import serial
from datetime import datetime
from pytz import timezone
import csv
import os

print('serial ' + serial.__version__)

PORT = '/dev/ttyACM0'
BaudRate = 9600

ARD = serial.Serial(PORT, BaudRate)

# Set the time zone for Seoul
seoul_tz = timezone('Asia/Seoul')

# Create a filename based on the current date
current_date = datetime.now(seoul_tz).strftime('%Y%m%d')
filename = f"{current_date}.csv"

# Specify the directory where the file will be saved
directory = "/home/desktop"  # Replace with your desired directory path

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Full path to the file
filepath = os.path.join(directory, filename)

# Create and open the CSV file for writing
with open(filepath, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['Timestamp', 'Humidity (%)', 'Temperature (DHT) (C)', 'Temperature (BMP280) (C)', 'Pressure (hPa)'])

    def Ardread():
        if ARD.readable():
            LINE = ARD.readline().decode('utf-8').strip()
            data = LINE.split()

            if len(data) == 5:  # Adjusted the length based on expected data fields
                # Get the current time in Seoul timezone
                now = datetime.now(seoul_tz)
                timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

                # Parse the data
                humidity = data[0]
                temp_dht_c = data[1]
                temp_bmp = data[3]
                pressure = float(data[4]) / 1000  # Assuming pressure is in Pa

                # Print the data
                print(f"Timestamp: {timestamp}")
                print(f"Humidity: {humidity}%")
                print(f"Temperature (DHT): {temp_dht_c}C")
                print(f"Temperature (BMP280): {temp_bmp}C")
                print(f"Pressure: {pressure} hPa\n")

                # Write the data to the CSV file
                writer.writerow([timestamp, humidity, temp_dht_c, temp_bmp, pressure])
            else:
                print("Error: Unexpected data format")
        else:
            print("Failed to read from serial port")

    while True:
        Ardread()
        time.sleep(5)  # Adjust the sleep time as needed
