# echo-server.py
# from https://realpython.com/python-sockets/#echo-client-and-server

import socket

HOST = "127.0.0.1"
PORT = 8000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    while True:
        s.listen()

        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
