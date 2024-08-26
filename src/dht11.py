import dht
import machine
from time import sleep

DHT_PIN = 2

def get_temperature_and_humidity():
    dht11 = dht.DHT11(machine.Pin(DHT_PIN))

    # measure twice because of cached data
    dht11.measure()
    sleep(2)
    dht11.measure()

    temperature = dht11.temperature()
    humidity = dht11.humidity()

    return temperature, humidity
