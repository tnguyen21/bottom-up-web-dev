# Bottom Up Web Dev: Week 2

## TCP/IP Requests

Recall from the previous chapter that TCP/IP are just protocols on how to package up bytes and send them over a network reliably.

`tcp-echo-client.py` and `tcp-echo-server.py` are dead simple examples of sending bytes over sockets.
The key thing to note is that Python (and many other languages) leverage TCP's notion of a _socket_ to represent that network connection.
In both the client and server, we are either sending or receiving _bytes_ over the _socket_.
Under the hood is code that actually manipulates and formats the bytes to be compliant with the TCP/IP protocols, re-requesting missing bytes, and so on.

As a web developer, we typically don't want to worry about every byte we're sending over the network.
In fact, we don't want to think of our application as bytes at all.
Applications can get complex quickly!
Instead, we want to think in terms of higher level abstractions, like HTML, CSS, an image file, a JavaScript framework, and so on.

In Python, when we want to send strings over a socket, there's a convenient short hand for turning that string into bytes.

```python
s = "this is a string"

s_bytes = b"this is a string that is turned into bytes"
```

Notes that `s_bytes` has a "b" right before the string.
This is Python's convenient way of converting a string into bytes, and we use it in `tcp-echo-client.py` to convert our message before sending it over the network.

Frameworks and libaries often do this implicitly.
Remember, we don't want to think in bytes if we don't have to!

## HTTP Requests

HTTP requests in HTTP 2.0+ have gotten [complicated](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).
Seriously, look at all those headers!

Instead, we'll look at what HTTP 0.9 requests were like, which can help us wrap our heads around the concept.
Remember, HTTP 1.0 and HTTP 2.0 (and eventually HTTP 3.0) built on top of this initial prototype.
All of the headers are meaningful in contemporary web applications, but you'll learn about them as you run up against them for the particular application your working on.
Odds are, you won't need to know about most of the headers for your day-to-day.

Anyway, without further ado, here's an HTTP 0.9 request:

```
GET /index.html
```

Yup!
That's it.
Really.

HTTP 0.9 only defined one type of request, "GET", which had to be in a particular format.
Specfically, the format defined special kinds of whitespace that had to be interleaved within the request so that receivers would know that this was an "HTTP request".
Recall, sockets are dealing with _bytes_, and unless both the sending and receiving software work together to define what order those bytes should arrive in, it's all noise.

In `http-request.py` on line 27, we see `socket.send` used to format a string and send it somewhere.

```python
s.send((f"GET {path} HTTP/1.0\r\n" +
        f"Host: {host}\r\n\r\n").encode("utf8"))
```

Notice the "\r" and "\n" characters -- those are white spaces to signify that it's an HTTP request.
Also note that we specify "Host" as part of our message.
This wasn't in the original HTTP 0.9 spec, but it's used here because modern servers (which you can use this script on!) expect it.

Go ahead and run `python http-request.py` with no changes on your command line.
You should hit `example.org` and get the whole HTML document printed out in your shell.

Look at that!
You just sent an HTTP request, and all it really was was a handful of bytes in a particular order.

## HTTP Servers

What about servers?

Well, we have a format for sending requests that we agreed upon.
As server implementers, it's now our job to gracefully interpret those bytes and recognize those requests, and error out on ones that don't comply.

You can find the gist of what this takes in `http-server.py`.
Particularly, notice how we handle multiple headers from a request, so we're going beyond HTTP 0.9.

Additionally, notice how there are [response codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).
You probable recognize some, like "200" for success or "404" for an error.
These are additions made in later versions of HTTP, which is why I'm not giving it a lot of discussion here.
But once you grasp the core idea of what sending a response requires, you can dig deeper into the details that are particular to whatever application you want to build.

## References

- [Building a basic HTTP Server from scratch in Python](https://joaoventura.net/blog/2017/python-webserver/)
- [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
- [Real Python: Socket Programming](https://realpython.com/python-sockets/)
