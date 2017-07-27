Project's checklist
-------------------

Purpose
=======

Foster continuous improvement within Sophilabs, by promoting a self-critical culture that thrives on welcoming and adapting to change. To do so, each Squad operates through basic quality tools (such as customized checklists), allowing each project a thorough process-alignment analysis against best practices for specific knowledge-domains like: Security, Software Design, Methodologies, etc.

Checklists are built on top of a simplified "Objectives & Key Results" approach, where expected results align with best practices and are validated by specific questions. In consequence, deviated results are visible and suggested action plans can be assessed and implemented. 

E.g.: "Does every team (and team member) subscribes to Agile management practices? - If not, assistance can be requested from the Agile Master to assess the team's knowledge gaps and implement Agile awareness workshops"


Security Checklist
==================

Please fill this document with items every project should complete according with the Security squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...


Testing Checklist
=================

- Implement unit testing in your project.
    - You can read the following guides for
      `Django <./../frameworks/django/testing.rst>`__ and
      `React <./../frameworks/react#testing>`__.
- Implement load testing.
- Measure code coverage.
- Run code coverage measurements automatically for each merge request.
    - Check out the `Gitlab documentation <https://docs.gitlab.com/ee/ci/>`__ for further information about continuous integration.
- Prevent merging if team-defined criteria is not met. (For example: coverage percentage below 90%)
- Run tests automatically in each merge request and prevent merging if they fail.
- Document your testing setup in the *manifiesto file*.


React projects
^^^^^^^^^^^^^^

- Implement component testing `Shallow rendering <http://guidelines.sophilabs.io/react#testing>`__.


Deployment Checklist
====================

Please fill this document with items every project should complete according with the Deployment squad.
i.e.: configuring tools, make sure something is being use, make sure some methodology is being applied, etc...


Methodologies Checklist
=======================

- Every team clearly understands and subscribes to `Agile <https://playbook.sophilabs.io/#the-agile-way>`__ management principles
- `Customer <https://playbook.sophilabs.io/#customer-availability>`__ inclusion as part of the team is essential for delivering the greatest product 
- Teams strive for a clear `Product Vision <https://playbook.sophilabs.io/#understanding-product-vision>`__ from the customer, focusing in value-added tasks
- Always deliver committed work by the agreed upon schedule
- Always create `Tasks <https://playbook.sophilabs.io/#tasks>`__ for every work item done (on Jira, Trello, Github or any other system agreed for the project)
- Include as much valuable info in your Tasks as you can  (e.g. Description, Priority, Reporter, Start Date/Time, End Date/Time)
- Each team meets often to inspect, adapt and continuously improve (Planning, `Daily Stand-Ups <https://playbook.sophilabs.io/#standups>`__, Reviews and `Retrospectives <https://playbook.sophilabs.io/#biweekly-retrospective>`__)
- Focus efforts on always adding value; automate valuable time-consuming tasks and remove non-valuable ones  


Software Design Checklist
=========================

Every project must have:

- Documentation
    - `High-level design <https://en.wikipedia.org/wiki/High-level_design>`__
    - `Class Diagram <https://en.wikipedia.org/wiki/Class_diagram>`__
    - `Entity relationship model <https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model>`__
- Development Process
    - At least 2 team members must be involved on the component design within a project
    - Validate designs with other team members
    - Reach experienced developers for guidence

Code Analysis Checklist
=======================

- For every language use linters tool to verify code style guidelines. If you are in doubt about which tool you should use, refer to each language guidelines page. e.g. `Javascript <https://guidelines.sophilabs.io/languages/javascript/>`__, `Python <https://guidelines.sophilabs.io/languages/python/>`__, `Sass <https://guidelines.sophilabs.io/languages/sass/>`__.
- Define Commit Message guidelines. For example ``/#\d+: [A-Z](\w|\s)*/`` (i.e. #555: Fix typo in guideline). You may find this `article <https://chris.beams.io/posts/git-commit/>`__ useful.
- Use commit hooks to verify the code style guidelines and the commit message by overriding the following files ``.git/hooks/pre-commit`` and ``.git/hooks/commit-msg`` respectively. Check out this `article <https://www.atlassian.com/git/tutorials/git-hooks>`__ to learn more about Git hooks.
- Your project must follow a clear branching strategy, like `Git Flow <https://danielkummer.github.io/git-flow-cheatsheet/>`__. 
    - The master branch, or the equivalent for the project must be protected, meaning all commits must be merged from feature branches.
    - Every commit must be made inside a particular branch that encapsulate that particular task.

- Code reviews should be a common practice to ensure code quality and attachment to the `guidelines <http://vintage.agency/blog/how-to-implement-code-review-process-in-a-web-development-team/>`__.
   - Code reviews must be enforced before merging code to the master branch.
   - Code reviews should follow the `guidelines <https://playbook.sophilabs.io/#code-reviews>`__ in the Sophilabs Playbook.

- Every project must have docmentation for new hires explaining the Tools needed for work and processes involved in the everyday work. This includes having a `README <https://gist.github.com/PurpleBooth/109311bb0361f32d87a2a>`__ and a `Contributing <https://gist.github.com/PurpleBooth/b24679402957c63ec426>`__ guidelines file. 

  - Development tools: Text editors, IDEs, Plugins
  - Required environment files
  - Procedures for installing Hooks
