# echo-client.py

import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", default="127.0.0.1")
    parser.add_argument("-port", default=8000)

    args = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, args.port))
    
    s.sendall(b"Hello, world") # note, this is in bytes!
    data = s.recv(1024)

    print(f"Received {data!r}")

    s.shutdown(socket.SHUT_RDWR)
    s.close()
