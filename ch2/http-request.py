"""
This file contains modified code from Web Browser Engineering.
https://browser.engineering/http.html
"""

import socket
import argparse
from pprint import pprint

def request(url, port=80):
    scheme, url = url.split("://", 1)

    if ("/" in url):
      host, path = url.split("/", 1)
      path = "/" + path
    else:
      host = url
      path = '/'

    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
    )

    s.connect((host, port))

    s.send((f"GET {path} HTTP/1.0\r\n" +
            f"Host: {host}\r\n\r\n").encode("utf8"))

    response = s.makefile("r", encoding="utf8", newline="\r\n")

    statusline = response.readline()
    version, status, explanation = statusline.split(" ", 2)
    assert status == "200", "{}: {}".format(status, explanation)

    headers = ""
    while True:
        line = response.readline()
        if line == "\r\n": break
        headers += line

    body = response.read()
    s.close()

    return headers, body

def load(url, port=80):
    headers, body = request(url, port)
    print("Headers:")
    print(headers)
    print("Body:")
    print(body)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", default="http://www.example.com/")
    parser.add_argument("-port", default=80)

    args = parser.parse_args()

    load(args.url, args.port)