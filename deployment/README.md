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

### Git Flow

GitFlow is a branching model for Git. It has attracted a lot
of attention because it is very well suited to collaboration
and scaling the development team.
You can learn more about it [reading this blog post](https://nvie.com/posts/a-successful-git-branching-model/).

## Environments

When you are developing a new application commonly you will have many environments with differents
versions. Each environment has a specific propouse and a owner. We recommend the definition of 5 enviroments.

- **Development:**

  The development environment is local to each developer and usually are deployed locally in a developer
  machine, instead of in the cloud.
  
  A development instance exists in each developer machine, which contains in development code of the
  features being worked.

- **Staging:**
  
  The stage `Staging` is based on the dev branch. It has the latest developed features as soon as they
  are finished and tested by the Development team. It is used for demos about features before they
  are rolled into the `Release Candidate`.
  
  The owner of this environment is the Development Team. They are able to upgrade it whenever they
  consider necesary.

  We recommend host this application with the same technology that uses production in order to prevent
  problems.

- **Release Candidate (RC):**

  The `RC` environment has stable features and it is generally updated when a development cycle (for
  example a sprint) ends.

  This environment is meant to be used by the product owner during the development to test and validate
  features released.

  The owner of this environment is the product owner, so it should be updated after he/her approves the
  features included in a version.

- **UAT:**

  The UAT environment is used for testing features by the QA team before pushing them into production.
  The ownership of this environment belongs to the product owner.
  The bugs found in this environment that must be solved should be treated as `hotfix`.

- **Production:**

  The production environment hosts the client data, meant to be used by Customers.
  It should not be used by developers.

## Versioning

Has a correct versioning system is important to has tracked the impact
of a new deploy. We suggest use [SemVer 2.0](http://semver.org/) , so
given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when incompatible API changes are introduced,
- MINOR version when functionality in a backwards-compatible manner
  are introduced and
- PATCH version when backwards-compatible bug fixes are introduced

## Continuous integration

A [continuous integration service](https://en.wikipedia.org/wiki/Continuous_integration) eases the
development workflow by automating tasks such as testing and deployment.

There are many CI tools, we suggest use [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/)
or [Jenkins](https://jenkins.io).

## Rollback plan

Having a rollback plan is important to ensure availability, especially when the system we are building
is running with real customers in a production environment. With a rollback plan we are able to deploy
a previous version of our app whenever is necessary.

When you define a rollback plan you should take care of the following tips:

- Keep your rollback plan well documented.
  - A rollback plan should be well documented in order that each member of the team could execute it.
    If the rollback is needed in a production environment, is important to have the ability of apply
    it ASAP.
    You can include in your project *manifesto file* the step by step guideline to execute the rollback.

- Maintain your application's versions identified.
  - Use [git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) to identify each version in your
    VCS.
  - If you are using [docker](https://www.docker.com/), store each version image in a repository. For
    example using [Docker regestry](https://docs.docker.com/registry/) or
    [Amazon Elastic Container Regestry](https://aws.amazon.com/ecr/).

- Create a `deploy version` script or `deploy version step` in your CI.
  - Having the ability to deploy a specific version in a specific environment is fundamental in a rollback
    plan.
  - If you are using [kubernetes](https://kubernetes.io/), you can implement this functionality using
    [Rolling back a deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment)
    feature.

- Have a database rollback plan.
  - If you have environments with customer data is important to have a database rollback plan.
  - Most of the database providers have features to store and restore backups of the data.
  - If you are using [RDS](https://aws.amazon.com/rds/) you can easily configure your
    [backup strategy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html).