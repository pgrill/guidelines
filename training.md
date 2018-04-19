# Training

## Purpose

In your first steps in Sophilabs you will be requested to implement a training project
([Ticket System](https://github.com/sophilabs/training)) in the context of our
[Apprenticeship Program](./apprenticeship-program/README.md).

The next guidelines will provide you the best practices that we recommend.

## Languages

We recommend developing the ticket system using [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/)
for the backend and [React](https://reactjs.org/) for the front end.

You should read and apply the following guidelines:

- [Python](./programming/languages/python/README.md)
- [JavaScript](./programming/languages/javascript/README.md)
- [Django](./programming/frameworks-and-libraries/django/README.md)
- [React](./programming/frameworks-and-libraries/react/README.md)

## Databases

Our recommendation is to use [PostgreSQL](https://www.postgresql.org/) to store the system data.
You can find information about how to install Postgres in our [Postgres Guidelines](./databases/README.md#postgresql)

## Testing

In Sophilabs we take care of testing in each project we develop. We think that have unit and integration
tests is important to prevent and debug annoying bugs.

For your training project we suggest you include some unit test in backend and frontend. Before
implementing the test you should read the [Unit test guidelines](./testing/README.md#unit-testing) and
the [Testing guidelines by language](./testing/languages/README.md).

## Docker

Most of the projects developed in Sophilabs are hosted using containers through [Docker](https://www.docker.com/).
You should read our [Containerization Guidelines](./infrastructure/README.md#containerization) if you
want include containers in your training project.

## Linters

If you have time and you want to improve the quality of the code you write you can include in your
project some linters.

We recommend include the linters as pre-commit [Git Hooks](https://git-scm.com/book/gr/v2/Customizing-Git-Git-Hooks)
using [gilp](https://www.npmjs.com/package/gilp).

Some of the linter we use in Sophilabs are [EsLint](https://eslint.org/) for javascript and [flake8](https://pypi.python.org/pypi/flake8)
for python.