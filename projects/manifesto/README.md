# Project's Manifesto

The project manifesto is a way for the project team to [TODO].

## How to implement a manifesto in my project?

Just download the `_TEMPLATE.md` file and fill the gaps.

## Example manifesto

# Sophia

Sophia is the internal management system of Sophilabs.

## Testing

We use Django's integrated testing system in order to perform unit testing to the project. You can find each app tests in the `<app-name>/tests.py` file and you can run the tests by running `manage.py test`.

In the hours management system client (JS + React) we use `mocha` along with `enzyme` to perform reducer and component tests.

## Deployment

In some-project, the app is deployed automatically by GitLab pipelines everytime a commit is pushed into the :code:`master` branch and it passes all the tests.

## Code analysis

Please, setup the Gilp pre-commit hook in order to run `pylint` and `eslint` everytime you commit code and ensure all code you write is linted.

## Branching and code review

You should work on a separate branch for each issue using the [Git Flow](https://github.com/nvie/gitflow)_ branching model and send a *Merge Request* to the `dev` branch in order for a teammate to review your code and merge it or request changes.

## Dependency management

In case you have to add dependencies to the project, 

- **Python:** We have three `.pip` files located in `setup/some_project/containers/django/requirements/`. One for `development`, one for `production` and a `base` one which is inherited by the other ones.
- - **JavaScript:** We have a common `package.json` file. If you use `yarn` instead of `npm`, please make sure you **do** commit the `yarn.lock` file.
