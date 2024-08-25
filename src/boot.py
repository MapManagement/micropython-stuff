import socket
import network
import json

sta_if = network.WLAN(network.STA_IF)

try:
    # disable own access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    with open("env.json") as env_file:
        # read access point credentials from env file
        env = json.load(env_file)
        ssid = env["network"]["ssid"]
        key = env["network"]["key"]

        if not sta_if.isconnected():
            print(f"SSID: {ssid}")
            print(f"Key: {key}")
            print("Connecting...")

            # connect to access point
            sta_if.active(True)
            sta_if.connect(ssid, key)

            while not sta_if.isconnected():
                pass
    
        print("Network configuration:", sta_if.ifconfig())
except OSError:
    print("Cannot find env.json")
except Exception as e:
    print("Something went wrong")
    print(e)
