# Server security guidelines

## SSH

TBD: Description de SSH and importance of have version 2 of protocol

SSH Guide [SSH Server
Configuration](https://wiki.archlinux.org/index.php/Secure_Shell#Configuration_2)

## HTTPS

You can read an intro on HTTPS
[here](https://en.wikipedia.org/wiki/HTTPS).

It's not enough to protect /sensitive/ resources only, all other pages
that can directly or indirectly link to said resources must be protected
also, so as to prevent man in the middle attacks.
[MTM](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)

You can read on how to configure HTTPs on some popular servers here:

- [Nginx HTTPS](https://nginx.org/en/docs/http/configuring_https_servers.html)
- [Apache SSL](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html)

Certificates for development:

- [Let's Encrypt](https://letsencrypt.org/)

## HSTS

You can read an intro [Mozilla Strict-Transport-Security][msts]

[msts]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security

Nginx setup:

- [Nginx HSTS](https://www.nginx.com/blog/http-strict-transport-security-hsts-and-nginx/)