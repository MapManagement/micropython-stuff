import machine
import socket

def site_humidity_json():
    humidity_json = ""
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

        response = humidity_json
        cl.send("HTTP/1.0 200 OK")
        cl.send(response)
        cl.close()
