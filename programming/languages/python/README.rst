Python guidelines
-----------------

Rules
=====

- Use 4 spaces for indentation.
- Please conform to the indentation style dictated in the .editorconfig file.
  We recommend using a text editor with EditorConfig support to avoid indentation
  and whitespace issues. Use the following `.editorconfig file <./files/.editorconfig>`__
  as a base configuration.
- Follow `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.
  Use `flake8 <https://pypi.python.org/pypi/flake8>`__ to check for problems in this area.
- In docstrings, follow `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`__.
-  Recommended ``flake8`` extensions:

   - flake8-mutable (Mutable default parameters in function definitions)
   - flake8-pep3101 (String formatting)
   - flake8-print (``print`` calls)
   - flake8-quotes (Enforce single quotes)
   - flake8-debugger (``pdb/ipdb`` traces)

Naming
======

+----------------------------+--------------------+-------------------------------------------------------------------+
| Type                       | Public             | Internal                                                          |
+============================+====================+===================================================================+
| Packages                   | lower_with_under   |                                                                   |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Modules                    | lower_with_under   | _lower_with_under                                                 |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Classes                    | CapWords           | _CapWords                                                         |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Exceptions                 | CapWords           |                                                                   |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Functions                  | lower_with_under() | _lower_with_under()                                               |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER                                                  |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Global/Class Variables     | lower_with_under   | _lower_with_under                                                 |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Instance Variables         | lower_with_under   | _lower_with_under (protected) or __lower_with_under (private)     |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Method Names               | lower_with_under() | _lower_with_under() (protected) or __lower_with_under() (private) |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Function/Method Parameters | lower_with_under   |                                                                   |
+----------------------------+--------------------+-------------------------------------------------------------------+
| Local Variables            | lower_with_under   |                                                                   |
+----------------------------+--------------------+-------------------------------------------------------------------+


Testing
=======

Visit the `testing </testing/automated/python/README.rst>`__ page.

References
==========

- https://docs.djangoproject.com/en/1.9/internals/contributing/writing-code/coding-style/
- https://google.github.io/styleguide/pyguide.html
