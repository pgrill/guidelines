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

- `Kick-off <./kick-off/README.rst>`__
    - `Projects manifesto <./kick-off/manifesto/README.rst>`__ **[Meta squad]**
    - `Software development workflow <./kick-off/workflow.rst>`__ **[Deployment squad]**
    - `Development environment <./kick-off/environment.rst>`__ **[Code analysis squad]**
    - `Docker setup <./kick-off/docker.rst>`__ **[Deployment squad]**
    - `Project bootstrapping <./kick-off/bootstrapping.rst>`__ **[Code analysis squad]**
- `Visual design <./visual-design/README.rst>`__ **[Visual design squad]**
- `Software design <./software-design/README.rst>`__ **[Software design squad]**
- `Databases <./databases/README.rst>`__ **[Databases squad]**
- `Security <./security/README.rst>`__ **[Security squad]**
- `Programming <./programming/README.rst>`__ **[Code analysis squad]**
- `Testing <./testing/README.rst>`__ **[Testing squad]**
- `Deployment <./deployment/README.rst>`__ **[Deployment squad]**
