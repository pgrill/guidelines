# Deployment

Each project that has medium complexity should have a clear deployment
process in order to allow launch a new release in a reliable and quick
way. With a correct deployment process you can detect bugs before
introducing it to a production environment.

## Version Control System

Every project must use a Version control systems (VCS). VCS are useful
to track the changes we made in our code and facilitates team
collaboration. [Git](https://git-scm.com) is our preferred VCS. We use
[GitHub](https://github.com) for open-source projects and
[GitLab](https://gitlab.com) for proprietary projects.

## Versioning

Has a correct versioning system is important to has tracked the impact
of a new deploy. We suggest use [SemVer 2.0](http://semver.org/) , so
given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when incompatible API changes are introduced,
- MINOR version when functionality in a backwards-compatible manner
  are introduced and
- PATCH version when backwards-compatible bug fixes are introduced

## Continuous integration

A [continuous integration
service](https://en.wikipedia.org/wiki/Continuous_integration) eases the
development workflow by automating tasks such as testing and deployment.

There are many CI tools, we suggest use [GitLab
CI](https://about.gitlab.com/features/gitlab-ci-cd/) or
[Jenkins](https://jenkins.io).