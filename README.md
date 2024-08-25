# Wemos Stuff

Some stuff with MicroPython on ESP8266 devices.

## Development

### picocom

(minicom seems to be a better choice)

Source: https://github.com/npat-efault/picocom

Connect to ESP8266 via REPL:

```sh
picocom /dev/ttyUSB0 -b115200
```

### rshell

Source: https://github.com/dhylands/rshell

Connect to ESP8266 and exchange files:

```sh
rshell -p /dev/ttyUSB0 -b 115200 -d
```
