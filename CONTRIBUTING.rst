Contributing
------------

Feel free to contribute to this guidelines within the scope of the following best practices.

Styling Rules
=============

- Introduce changes by creating pull requests and assigning them to the targeted content's owning squad
- Avoid copying content from other sources, just link it
- If you are going to upload code snippets, make sure that they respect the PEP8 standard by running linters on it
- Be concise
- Use bullet-lists extensively

Some useful tools for contributing are:

- `restview <https://github.com/mgedmin/restview>`__

  A viewer for ReStructuredText documents that renders them on the fly.

  .. code-block:: bash

      pip install restview
      restview .

File and folder names
=====================

Lowercase, hyphenated file and folder names, i.e. `code-reviews.rst`.

rST guidelines
==============

Headings
^^^^^^^^

* Use ``------`` for level 1 headings.
* Use ``======`` for level 2 headings.
* Use ``^^^^^^`` for level 3 headings.
* Use ``++++++`` for level 4 headings.

Ownership
=========

Guidelines is divided into different sections, and each section has an owner.
The owners are responsible for the content of those areas, every pull request
that affects an area should be assigned to the corresponding owner.

This is the current ownership configuration:

- `Project kick-off <./kick-off/README.rst>`__
    - `Projects manifesto <./kick-off/manifesto/README.rst>`__ **[Meta squad]**
    - `Software development workflow <./kick-off/workflow.rst>`__ **[Deployment squad]**
    - `Development environment <./kick-off/environment.rst>`__ **[Code analysis squad]**
    - `Docker setup <./kick-off/docker.rst>`__ **[Deployment squad]**
    - `Project bootstrapping <./kick-off/bootstrapping.rst>`__ **[Code analysis squad]**

- `Software design <./software-design/README.rst>`__
    - `Principles <./software-design/principles.rst>`__ **[Software design squad]**
    - `Best practices <./software-design/best-practices.rst>`__ **[Software design squad]**

- `Databases <./databases/README.rst>`__
    - `Best practices <./databases/best-practices.rst>`__ **[Databases squad]**

- `Security <./security/README.rst>`__
    - `Best practices <./security/best-practices.rst>`__ **[Security squad]**

- `Programming <./programming/README.rst>`__
    - `Languages <./programming/languages/README.rst>`__ **[Code analysis squad]**
        - `Python <./programming/languages/python/README.rst>`__
        - `JavaScript <./programming/languages/javascript/README.rst>`__
        - `SASS <./programming/languages/sass/README.rst>`__
        - `HTML <./programming/languages/html/README.rst>`__
    - `Frameworks and libraries <./programming/frameworks-and-libraries/README.rst>`__ **[Code analysis squad]**
        - `Django <./programming/frameworks-and-libraries/django/README.rst>`__
        - `React <./programming/frameworks-and-libraries/react/README.rst>`__
    - `Code reviews <./programming/code-reviews.rst>`__ **[Code analysis squad]**

- `Testing <./testing/README.rst>`__
    - `Automated testing <./testing/automated/README.rst>`__ **[Testing squad]**
        - `Python <./testing/automated/python/README.rst>`__
    - `QA reviews <./testing/qa-reviews.rst>`__ **[Testing squad]**

- `Deployment <./deployment/README.rst>`__
    - `Versioning <./deployment/versioning.rst>`__ **[Deployment squad]**
    - `Continuous integrations <./deployment/continuous-integration.rst>`__ **[Deployment squad]**
    - `Containerization <./deployment/containerization.rst>`__ **[Deployment squad]**
