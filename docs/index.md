# uncle-archie

![uncle archie](images/unclearchiebk.svg)

**Uncle Archie** is a home-brewed continuous integration server.
It handles pull request checks (build-test) and push-to-deploy 
functionality (build-test-deploy). It is written in Python
and uses PyGithub.

**Uncle Archie** is intended to run behind an nginx reverse proxy
so that SSL can be used. This requires that the server running 
Uncle Archie be accessible via a domain name, and not just a bare 
IP address.

Documentation: <https://pages.charlesreid1.com/uncle-archie> or [`docs/index.md`](docs/index.md)

Source code: <https://git.charlesreid1.com/bots/uncle-archie>

Source code mirror: <https://github.com/charlesreid1/uncle-archie>

## Table of Contents

* [Architecture of Uncle Archie](arch.md)

