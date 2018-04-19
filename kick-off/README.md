# Project Kick-off

Here you will find some useful resources that may help you and your team to
kick-off your project.

## Project's Manifesto

Your project manifesto is a document targeted mostly to newcomers
so they can start working without inconvenience.

Your project's manifesto should include all necessary instructions in order to
set up the project, run it, run tests, etc.

### How to implement a manifesto in my project

Just download the following [template](./TEMPLATE.md) file and adapt it to your project.

## Development workflow guidelines

## GitFlow

We follow Gitflow's branching model for our projects. You can read about
it [here](http://nvie.com/posts/a-successful-git-branching-model/).

## Continuous Delivery

Continuous Delivery (CI) is the ability to get changes of all types (including
new features, configuration changes, bug fixes and experiments) into production,
or into the hands of users, safely and quickly in a sustainable way. We
recommend every project to set up a CI.

* Prefer the CI tool to be owned by the client itself.
* If your client doesn't provide a CI tool, you can use Sophilabs's own
  [Jenkins CI](https://ci.sophilabs.io/).

## Docker

We prefer containerizing our applications using
[Docker](https://www.docker.com/), and
[Docker Compose](https://docs.docker.com/compose/) for more complex
applications.

You can start your app find some good Docker Compose
[examples](https://docs.docker.com/compose/samples-for-compose/) for Django.
For specific applications you can also refer to the Docker
[samples](https://docs.docker.com/samples/) page.

## Setting up macOS

If just got a new MacBook, you should set up it correctly. This
list covers the bare minimum requirements for developing a web
application in a macOS based system.

1. Install [Slack](https://slack.com/downloads/osx) and [sign
   up](https://sophilabs.slack.com/) with your sophilabs email address.
2. Install the [Homebrew](https://brew.sh/) package manager for
   installing applications or utilities.
3. macOS only comes with Python 2 installed. Install the latest Python
   3 release from the
   [website](https://www.python.org/downloads/mac-osx/).
4. Avoid installing Python packages at the system level, use virtual
   environments instead. See
   [here](https://docs.python.org/3/tutorial/venv.html#introduction)
   why this is the recommended approach. There are several options for
   creating/managing virtual environments, we recommend
   [pyenv](https://github.com/pyenv/pyenv).
5. Feel free to install and use your favorite text editor or IDE. If
   you don't have one, we recommend PyCharm to get started.
6. Install the latest LTS version of [Node.js](https://nodejs.org/en/)
   if you're going to work with JavaScript.
7. Install [Docker for
   Mac](https://docs.docker.com/docker-for-mac/install), use the edge
   version if you need better integration with docker cloud.
8. Setup a pair of ssh keys with your sophilabs email address. You can
   follow [this
   guide](https://help.github.com/articles/connecting-to-github-with-ssh/)
   if you're not sure how to do it. You will use these keys to push
   content to our Gitlab server or Github repositories, and also for
   accessing any remote server you need to access when working on a
   project.

## Project bootstrapping

### Project directory structure

* A project divided into different git repos is hard to maintain,
  avoid it.

### Docker

#### How to organize Docker files

We recommend to use the following folder structure to organize your docker files.

```text
.
├── compose
│   ├── build.sh
│   ├── docker-compose.base.yml
│   ├── docker-compose.dev.yml
│   ├── docker-compose.prod.yml
│   └── up.sh
└── projects
    ├── api
    │   └── Dockerfile
    ├── db
    │   └── Dockerfile
    ├── proxy
    │   └── Dockerfile
    └── frontend
        └── Dockerfile
```

In order to use an environment `docker-compose` file,
you will need to chain them with the `base` one, like this:

```bash
docker-compose -f docker-compose.base.yml -f docker-compose.dev.yml [subcommand] <args>
```

### Commit hooks

We recommend to let [Gilp](https://github.com/sophilabs/gilp) handle that for you.

You can run linters, check commit messages and more with Gilp and Gulp.

## References

1. [Try Git](https://try.github.io/)
2. [Pro Git](https://git-scm.com/book/)
