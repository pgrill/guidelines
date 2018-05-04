# Training

## Purpose

In your first steps in Sophilabs you will be requested to implement a
([Training Project](https://github.com/sophilabs/training)) in the context of our
[Apprenticeship Program](./apprenticeship-program/README.md).

The next guidelines will provide you the best practices that we recommend.

## Languages

We recommend developing the training project using [Python](./programming/languages/python/README.md)/[Django](./programming/frameworks-and-libraries/django/README.md)
for the backend and [React](./programming/frameworks-and-libraries/react/README.md) for the frontend.

You should read and apply the following guidelines:

- [Python](./programming/languages/python/README.md)
- [JavaScript](./programming/languages/javascript/README.md)
- [Django](./programming/frameworks-and-libraries/django/README.md)
- [React](./programming/frameworks-and-libraries/react/README.md)

## Databases

Our recommendation is to use some of the databases we suggest in our [Databases guidelines](./databases/README.md).
For this project we strongly recommend using [Postgres](./databases/README.md#postgresql).

## Testing

In Sophilabs we take care of testing in each project we develop. We think that have unit and integration
tests is important to prevent and debug annoying bugs.

For your training project we suggest you include some unit test in backend and frontend. Before
implementing the test you should read the [Unit test guidelines](./testing/README.md#unit-testing) and
the [Testing guidelines by language](./testing/languages/README.md).

## Docker

Most of the projects developed in Sophilabs are hosted using containers through Docker.
You should read our [Containerization Guidelines](./infrastructure/README.md#containerization) if you
want include containers in your training project.

## Linters

If you have time and you want to improve the quality of the code you write you can include in your
project some [linters](./code-analysis/README.md#linters) to ensure the quality of your code.

We recommend include the linters as  [pre-commit git hooks](./code-analysis/README.md#commit-hooks)
using [gilp](https://www.npmjs.com/package/gilp).