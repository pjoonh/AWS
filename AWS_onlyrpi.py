import Adafruit_DHT

def DHT_sensor():
    sensor = Adafruit_DHT.DHT11

    pin = 2 # Data핀의 GPIO핀 number

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)   # 센서값(온도, 습도) 읽기

    if humidity is not None and temperature is not None:   #습도 및 온도 값이 모두 제대로 읽혔다면 
        print(f'Temp = {0:0.1f}℃\nHumidity = {1:0.1f}%\n'.format(temperature, humidity))  # 온도, 습도 순으로 표시
    else:                                                  # 에러가 생겼다면 
        print('Failed.')        #  에러 표시
        
start_command = input('Start?(T/F) :')
if start_command == 'T':
    while True:
        DHT_sensor()
elif start_command == 'F':
    print('Not running')
else:
    print('You entered it incorrectly.')