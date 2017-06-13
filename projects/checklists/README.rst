Security Checklist
==================

Please fill this document with items every project should complete according with the Security squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...

Testing Checklist
=================

- Implement unit testing in your project.
- You can read the following guides for `Django <https://guidelines.sophilabs.io/frameworks/django/test>`_ and `React <https://guidelines.sophilabs.io/react#testing>`_.
- Implement load testing. 
- Measure code coverage.
- Run code coverage measurements automatically for each merge request.
	- Optionally: Prevent merging if team-defined criteria is not met. (For example: coverage percentage below 90%)
- Run tests automatically in each merge request and prevent merging if they fail.
- Document your testing setup in the *manifiesto file*.

React projects
--------------

- Implement component testing `Shallow rendering <http://guidelines.sophilabs.io/react#testing>`_.

Deployment Checklist
====================

Please fill this document with items every project should complete according with the Deployment squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...

Methodologies Checklist
=======================

Please fill this document with items every project should complete according with the Methodologies squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...

Software Design Checklist
=========================

Please fill this document with items every project should complete according with the Software Design squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...

Code Analysis Checklist
=======================

- For every language use linters tool to verify code style guidelines. The following
  tools are preferred:
 - `flake8` for Python.
 - `eslint` for Javascript.
 - `scsslint` for Sass.
 - `htmllint` for HTML.
 - `credo` for Elixir.
- Define Commit Message guidelines. For example `/\d+: [A-Z](\w|\s)*\./` (e.g. 555: Title finished by a dot character.).
- Use commit hooks to verify the code style guidelines and the commit message by overriding the following files `.git/hooks/pre-commit` and `.git/hooks/commit-msg` respectively.
- The master branch, or the equivalent for the project must be protected, meaning all commits must be merged from feature branches
- Every commit must be made inside a particular branch that encapsulate that particular task.
- Code reviews must be enforced before merging code to the master branch.
- Code reviews should follow the guidelines in the Sophilabs Playbook.
- Every project must have a README file for new hires explaining the Tools needed for work and processes involved in the everyday work. This includes
    - Development tools: Text editors, IDEs, Plugins
    - Required environment files
    - Procedures for installing Hooks
