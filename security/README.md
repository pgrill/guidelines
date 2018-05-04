# Security

Here you will find useful information related to information security.

Keeping security standards up to date is very important to keep your
project's information integrity and reliability.

## Server security

### SSH

SSH (Secure Shell) is an encrypted network protocol.
Commonly used for remote login to servers.

SSH Guide: [SSH Server
Configuration](https://wiki.archlinux.org/index.php/Secure_Shell#Configuration_2)

### HTTPS

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

### HSTS

You can read an intro [Mozilla Strict-Transport-Security][msts]

Nginx setup:

- [Nginx HSTS](https://www.nginx.com/blog/http-strict-transport-security-hsts-and-nginx/)

## Database security

- [AWS RDS Guide][apg]
- [Azure Guide](https://azure.microsoft.com/en-us/campaigns/developer-guide/)

## Security patches

Keeping your application reliability is very important for both
Sophilabs and the customer. So we must ensure we have the latest
security patches and fixes applied as soon as possible.

- [Notify patches](https://packages.debian.org/search?keywords=apticron).
- Subscribe to security maillists such as [Ubuntu Security Announces](https://lists.ubuntu.com/mailman/listinfo/ubuntu-security-announce).

## Identity and Access Management Guidelines

### User information storage

- Use a password hashing algorithm such as `bcrypt` in order to
  avoid user data stealing from a database leak.
- When using external identity providers such as Facebook or Google,
  carefully check what permission scopes are you requesting. An user
  may cancel the authentication flow if you're requesting too much personal information.

### Login

- If you are developing an API, use [JSON Web Tokens][jwt] (JWT) to secure it
  instead of personal access tokens.
- Do not overload the JWT token with user info, keep in mind that the
  `accessToken` with be included in every request to the API.
  Instead, use an `idToken` (a JWT issued to hold user information) along with your `accessToken`.
- Do not issue "non-expiring tokens". The lifespan of the token may
  vary depending on the project and its feature set.
- Always use HTTPS when sending sentitive data, even if it is
  between servers.
- Implement two-factor authentication if it's possible, it adds an
  extra layer of security.
- Implementing an OAuth 2 server is a good idea if you plan to let
  other applications connect with yours through an open API.

### Passwords

#### Password creation

- Avoid auto-generating passwords. Instead, ask the user to define one
  during signup.
- Create a minimum password complexity policy and ask the user to choose
  a password that he/she does not use anywhere else.

#### Password reset

- Avoid using "personal questions" to reset the users' passwords.
- Ask for the user's current password if the user is logged in.
- Send a password reset link to the user if he/she claims to have
  forgotten its current one.

#### Store and share passwords

- Store and share passwords in a secure way in very important.
- Don't send password by email, use a secure password manager. We recommend use
  [1password](https://1password.com/).

[jwt]: (https://jwt.io/)
[msts]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
[apg]: http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html