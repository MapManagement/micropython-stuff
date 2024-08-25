import socket
import network
import json

sta_if = network.WLAN(network.STA_IF)

try:
    with open('env.json') as env_file:
        env = json.load(env_file)
        ssid = env["network"]["ssid"]
        key = env["network"]["key"]

        if not sta_if.isconnected():
            print('Connecting...')

            sta_if.active(True)
            sta_if.connect(ssid, key)

            while not sta_if.isconnected():
                pass
    
        print('Network configuration:', sta_if.ipconfig('addr4'))
except OSError:
    print("Cannot find env.json")
except Exception:
    print("Something went wrong")
