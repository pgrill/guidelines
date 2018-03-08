# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for
development and testing purposes. See deployment for notes on how to deploy the project on a live
system.

### Prerequisites

What things you need to install the software and how to install them

```text
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```text
Give the example
```

And repeat

```text
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Security

When you start working with your development environment, you will have an admin user predefined.

```text
user: admin@pt.com
password: admin
```

For storing and sharing secure passwords we use [1Password](https://agilebits.com/onepassword). Ask
your principal to give you access for the needed services and environments passwords.

You also need to create a ssh key and ask your principal to include it in the staging server.

## Testing

We use Django's integrated testing system in order to perform unit testing to the project. You can
find each app tests in the `<app-name>/tests.py` file and you can run the tests by running
`manage.py test`.

In the hours management system client (JS + React) we use `mocha` along with `enzyme` to perform
reducer and component tests.

**Backend coverage**: We use `coverage.py` in order to perform backend code coverage measurement.
You can measure the code coverage by running `coverage run --source="." manage.py test` in the
folder where `manage.py` is located. Then, generate a report in the format you decide,
for example: `coverage html`.

**Frontend coverage**: We use `codecov` in order to perform JavaScript code coverage measurement.
Run `npm run test` to run the tests along with a coverage report.

## Deployment

### Traceability

The project uses Git as the version control system and GitHub/GitLab for development platform
following the Git Flow’s branching model.

An up-to-date changelog can be found [here](./CHANGELOG.md).

### Portability

In order to improve the project’s portability it is using Docker and Docker Compose as the
containerization solution.

### Visibility

GitLab CI/Jenkins is used as the continuous integration system.
CI is configured for every environment such as dev, RC, and prod.

- The development server can be found [here](https://<subdomain>.sophilabs.me)
- The RC server can be found [here](https://<subdomain>.sophilabs.me)
- CI dashboard can be found [here](https://<subdomain>.sophilabs.me)
- Full deployment process and tools documentation can be found [here](DEPLOYMENT.md)

CI notifications are configured to send build statuses via Slack/email.

### Reversibility

Database backups are automatically created every <days> days.

The project can be automatically downgraded. The rollback plan can be found [here](DEPLOYMENT.md).

To prevent server downtime the project is using Docker Swarm for deployment.

## Code analysis

Describe the tools used to check the code before a commit is done. For example using gilp or
another tool.

## Branching and code review

We work in separate branch for each issue using the [Git Flow](https://github.com/nvie/gitflow)
branching model and send a *Merge Request* to the `dev` branch in order for a teammate to review
your code and merge it or request changes. Describe the naming convention for branches like:

- 1234: Feature description.

### Code Review

Describe your code review process here, if you have any. An example could be dhe following one.
Refer to the Playbook for code review guidelines.

1. Make commit to your repository.
2. A developer downloads your code and test it.
3. After the review is done, we merge the code to dev.

## Dependency management

In case you have to add dependencies to the project,

- **Python:** We have three `.pip` files located in
  `setup/some_project/containers/django/requirements/`. One for `development`, one for `production`
  and a `base` one which is inherited by the other ones.
- **JavaScript:** We have a common `package.json` file. If you use `yarn` instead of `npm`, please
  make sure you **do** commit the `yarn.lock` file.
- **Elixir:** We use mix, and hex for dependency management.