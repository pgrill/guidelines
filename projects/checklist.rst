Project's checklist
-------------------

Purpose
=======

TBD


Security Checklist
==================

Please fill this document with items every project should complete according with the Security squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...


Testing Checklist
=================

- Implement unit testing in your project.
    - You can read the following guides for
      `Django <./../frameworks/django/testing.rst>`_ and
      `React <./../frameworks/react#testing>`_.
- Implement load testing.
- Measure code coverage.
- Run code coverage measurements automatically for each merge request.
- Prevent merging if team-defined criteria is not met. (For example: coverage percentage below 90%)
- Run tests automatically in each merge request and prevent merging if they fail.
- Document your testing setup in the *manifiesto file*.


React projects
^^^^^^^^^^^^^^

- Implement component testing `Shallow rendering <http://guidelines.sophilabs.io/react#testing>`_.


Deployment Checklist
====================

Please fill this document with items every project should complete according with the Deployment squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...


Methodologies Checklist
=======================

- Every team clearly understands and subscribes to `Agile <https://playbook.sophilabs.io/#the-agile-way>`_ management principles
- `Customer <https://playbook.sophilabs.io/#customer-availability>`_ inclusion as part of the team is essential for delivering the greatest product 
- Teams strive for a clear `Product Vision <https://playbook.sophilabs.io/#understanding-product-vision>`_ from the customer, focusing in value-added tasks
- Always deliver committed work by the agreed upon schedule
- Always create `Tasks <https://playbook.sophilabs.io/#tasks>`_ for every work item done (on Jira, Trello, Github or any other system agreed for the project)
- Include as much valuable info in your Tasks as you can  (e.g. Description, Priority, Reporter, Start Date/Time, End Date/Time)
- Each team meets often to inspect, adapt and continuously improve (Planning, `Daily Stand-Ups <https://playbook.sophilabs.io/#standups>`_, Reviews and `Retrospectives <https://playbook.sophilabs.io/#biweekly-retrospective>`_)
- Focus efforts on always adding value; automate valuable time-consuming tasks and remove non-valuable ones  


Software Design Checklist
=========================

- Every project must have:
    - Documentation:
        - `High-level design <https://en.wikipedia.org/wiki/High-level_design>`_
        - `Class Diagram <https://en.wikipedia.org/wiki/Class_diagram>`_
        - `Entity relationship model <https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model>`_
    - Development Process
        - At least 2 team members must be involved on the component design within a project
        - Validate designs with other team members
        - Reach experienced developers for guidence

Code Analysis Checklist
=======================

- For every language use linters tool to verify code style guidelines. If you are in doubt about which tool you should use, refer to each language guidelines page. e.g. `Javascript <https://guidelines.sophilabs.io/languages/javascript/>`_, `Python <https://guidelines.sophilabs.io/languages/python/>`_, `Sass <https://guidelines.sophilabs.io/languages/sass/>`_.
- Define Commit Message guidelines. For example ``/#\d+: [A-Z](\w|\s)*/`` (i.e. #555: Fix typo in guideline). You may find this `article <https://chris.beams.io/posts/git-commit/>`_ useful.
- Use commit hooks to verify the code style guidelines and the commit message by overriding the following files ``.git/hooks/pre-commit`` and ``.git/hooks/commit-msg`` respectively. Check out this `article <https://www.atlassian.com/git/tutorials/git-hooks>`_ to learn more about Git hooks.
- Your project must follow a clear branching strategy, like `Git Flow <https://danielkummer.github.io/git-flow-cheatsheet/>`_. 
    - The master branch, or the equivalent for the project must be protected, meaning all commits must be merged from feature branches.
    - Every commit must be made inside a particular branch that encapsulate that particular task.

- Code reviews should be a common practice to ensure code quality and attachment to the `guidelines <http://vintage.agency/blog/how-to-implement-code-review-process-in-a-web-development-team/>`_.
   - Code reviews must be enforced before merging code to the master branch.
   - Code reviews should follow the `guidelines <https://playbook.sophilabs.io/#code-reviews>`_ in the Sophilabs Playbook.

- Every project must have docmentation for new hires explaining the Tools needed for work and processes involved in the everyday work. This includes having a `README <https://gist.github.com/PurpleBooth/109311bb0361f32d87a2a>`_ and a `Contributing <https://gist.github.com/PurpleBooth/b24679402957c63ec426>`_ guidelines file. 

  - Development tools: Text editors, IDEs, Plugins
  - Required environment files
  - Procedures for installing Hooks
