import dht11
import machine
import socket

def build_html(temperature, humidity):
    html = f"""
        <!DOCTYPE html>
        <html>
        <body>

        <h1>Temperature</h1>
        <p>{temperature}C</p>

        <h1>Humidity</h1>
        <p>{humidity}%</p>

        </body>
        </html>
    """

    return html

def site_humidity_json():
    socket_listen_port = 80
    socket_listen_ip = "0.0.0.0"

    addr = socket.getaddrinfo(socket_listen_ip, socket_listen_port)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print(f"Socket is listening on port {socket_listen_port} on IP {socket_listen_ip}", addr)

    while True:
        cl, addr = s.accept()

        print("Client connected from", addr)

        cl_file = cl.makefile('rwb', 0)

        while True:
            line = cl_file.readline()

            if not line or line == b"\r\n":
                break

        temperature, humidity = dht11.get_temperature_and_humidity()

        html = build_html(temperature, humidity)
        response = html

        cl.send(response)
        cl.close()
