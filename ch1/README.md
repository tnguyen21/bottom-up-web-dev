# Bottom Up Web Dev: Week 1

## Background

The idea for this material sprung up after being dissatisfied with how I was taught web development in a university course.
There were lots of interconnecting ideas in computer science that, in hindsight, should've been woven together but weren't.
This is my attempt at putting together some of those ideas, mostly for my reference and education.

There will be lots of toy examples and scripts based on the lower level ideas throughout this repo.
I found that as I progress in my career, I'll naturally specialize and dig into the topics that genuinely interest me.
For everything else, I can read about the core ideas and write some code to poke at it.
And that will usually suffice.
If I truly need to dig deep into the interals of something, I'll cross that bridge when I get there.

## Some History

There are more than enough people who have written about the history of the Internet.
I'll spare you the reading and ask you refer below to the Wikipedia page and link to the chapter of High Performance Browser Networking for more details.

Here we're going to focus on some high level ideas and dates.

### 1974: TCP/IP

There are two core protocols that power today's internet: the Transmission Control Protocol (TCP) and the Internet Protocol (IP).
Fundamentally, these two protocols figure out how to _reliably_ send bytes over potentially unreliable infrastructure.

IP concerns itself with the format of those bytes and giving identifiers to every machine that wants to send bytes.
This is why we refer to devices as having "IP" address, either in IPv4 or IPv6 naming schemes.

TCP focuses on how to send and receive bytes that are in IP-kosher format.
Because the underlying wired and wireless connections that send these pulses of electricty can be unreliable, TCP is a scheme to ensure that we receive _all_ the bytes in a message _in the correct order_.
In addition to making sure that network messages are reliably received, TCP provides an abstraction that applications can use to receive and interpret those bytes.

These two protocols power _a lot_ of the web.
It's worth being aware of them, even if you never have to dig too deep into their internals.

### 1990: HTTP and HTML

Tim Berners-Lee begins designing the HypterText Transfer Protocol (HTTP), HypterText Markup Language (HTML), and a Web browers.
Building ontop of TCP/IP, HTTP set a series of standards for how to transmit documents (HTML) which contained multiple medias (text, images).

The first proposal was for HTTP 0.9, which has some recognizable features of HTTP today, but is still fairly different from the HTTP used in contemporary applications.
Many applications today use HTTP 2.0, which added additional features and protocols.
There are some conversations of migrating to HTTP 3.0 to remedy some performance issues that were inherited from previous iterations of HTTP.

### 1990: Browsers

The first web browser was built by Tim Berners-Lee in 1990 at the same time he proposed HTTP and HTML.

This sparked what is now known as the "browser wars" of the 1990s, where many companies and organizations implemented their own browsers and tried to get on as many devices as possible.
Some of these browsers were proprietary, such as the one built by Netscape.
Eventually, the Mozilla Foundation created an open-sourced browser that evolved into what we now know as Firefox.

It's worth noting that as web developers, we often approach browsers from a "users" perspective.
Web developers are often concerned with the features browsers support, and if they'll support the code that they write for their applications.

However, it can be useful to consider the browser from a developer's perspective.
Consider the various operating system calls, network and memory management, and graphic rendering that a browser must do.
Someone had to write that code (it might be you one day)!

### 1995: JavaScript

JavaScript is a programming language that evolved out of the need to make websites more "dynamic".
Prior to JavaScript, websites were (for the most part) digital bill boards.
JavaScript was created primarily by Brendan Eich working at Netscape.

JavaScript was eventually adopted into other browsers during the browser wars.
It became a critical feature to support as more applications began using JavaScript to enable many of the use cases we see today (querying databases, managing user accounts, etc).

Eventually, JavaScript found its way beyond the web browser.
The language has evolved into an entire programming environment of its own, with the most common implementation of JavaScript being V8.
Now, in addition to being used to make websites dynamically render content, JavaScript can be used on servers, in embedded devices, and more.

## References

- [Internet - Wikipedia](https://en.wikipedia.org/wiki/Internet#History)
- [Brief History of HTTP - High Performance Browser Networking](https://hpbn.co/brief-history-of-http/)
- [How does the Internet work? - MDN](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work)
- [The World Wide Web project](http://info.cern.ch/hypertext/WWW/TheProject.html)
