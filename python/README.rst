Table of Contents
=================

#. `Rules`_
#. `Tests`_


Rules
=====

#. Use four spaces for indentation.
#. Please conform to the indentation style dictated in the .editorconfig file.
   We recommend using a text editor with EditorConfig support to avoid indentation
   and whitespace issues. User the following `.editorconfig file <./files/.editorconfig>`__
   as a base configuration.
#. Follow `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.
   Use `flake8 <https://pypi.python.org/pypi/flake8>`__ to check for problems in this area.
#. In docstrings, follow `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`__.


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



Tests
=====

    Python :code:`v3.3` or higher is assumed.

Testing is very important. Not only to prevent and debug annoying bugs but it also helps
project newcomers to better understand the expected functionality of your functions and
classes.

In the python world, testing is embraced. Its part of the standard.

:code:`unittest` is  the python standard module which provides a lot of useful
helpers to make writing test easy.

    **A note on Doctest**

    :code:`doctest` is a python module that will search for text that looks
    like an :code:`python` on your docstrings and execute it, if the result of
    that execution defers from the execution described in the docstrings then
    the module will fail.

    It may be a good way to document your code (although a proper docstring should
    be enough), but its not enough to test all cases correctly, so we avoid using
    them.


Project structure and configuration
-----------------------------------

**Folder structure**

When creating a python project (library, app, etc), its always good to define
a project root directory, from which all the console commands are going to be
executed, and then different folders for each module that represent different logic
or scope. So, following that, we could take four different approaches:

#. tests could all be contained in a :code:`test` folder inside the root directory
#. tests could all be contained in a :code:`test.py` file in the root directory
#. tests could be in a :code:`test.py` file inside each module, testing only that module
#. tests could be in a :code:`test` folder inside each module

    When using folders, test files should be named :code:`test.py` or
    :code:`test_<something>.py` to indicate what the file is testing.

Any of those approaches is valid, it depends on what kind of project its being developed and
the size of it. As a general rule, for apps, the test folder per module approach if preferred,
for medium projects the test folder on the root directory is a good choice, for everything
else, its up to the developers to make the call.

**Configurations**

Configuration, in general, depends on the tools/framework your app is using. If
the project depends on no framework, then (on most cases) no configuration is needed
as python already comes with a lot of testing helpers.

When using :code:`unittest`, running
:code:`$ python -m unittest` on the root directory will find all the tests located
in any of the ways defined above.

To make things easier, we tend to create a script that runs the test for us. If
we need to set same env variables or do something after or before running the tests
this is the file to do it.

.. code:: bash

    #!/bin/bash

    # <root_directory>/test.sh

    # Here we can set env variables
    # We could add test coverage, post test scripts or anything we need and the
    # devs won't have to change their working flow, just running test.sh will
    # test their code
    python -m unittest "$@"

If using that script, now running tests is a simple as running :code:`./test.sh` on
the root directory.


Unit tests
----------

Unit testing is a broad topic, a lot can be said about it. In its core, it means
testing isolated functions, avoiding to test the way it communicates with other parts
of the app.

In python, for us, that means using the :code:`unittest` module.

We'll build a simple library to sluggify text and show how what practices we
prefer to use when testing.

A sluggify function should take in some text and return a web safe representation
of that text. Let define a :code:`slug.py` file first.

.. code:: python

    # <project_root>/slug.py

    # Most basic implementation, no logic, takes a string and returns a string
    def sluggify(text):
        """Returns a slug based on ``text``"""
        return text

Now lets write our test to make sure our library is working correctly.

.. code:: python

    # <project_root>/tests/test_slug.py

    # python standard library for testing
    import unittest

    # the root directory is the folder from where the test are ran, this is
    # usually the project root directory so your imports should be relative to it.
    from slug import sluggify

    # All your tests suits should extend unittest.TestCase
    # it provides a handful of nice utilities to test your code, including
    # assertions and lifecycle events
    class TestSluggify(unittest.TestCase):
        """Tests for slug.slugify"""

        # Its important to test each case, edge cases included. This is where
        # test will help us with those hard-to-debug bugs.
        def test_empty_text(self):
            """Test that the slug of an empty string is an empty string."""

            # `assertEqual` asserts both expressions are equal.
            self.assertEqual(sluggify(''), '')

        def test_all_invalid_chars_text(self):
            """Test that the slug of an invalid text is an empty string."""
            self.assertEqual(sluggify(' ---*?/'), '')

        def test_all_valid_chars_text(self):
            """Test that the slug of a valid text is that same text."""
            self.assertEqual(sluggify('valid-slug'), 'valid-slug')

        # Test names should be descriptive, don't be afraid of long method names
        def test_mix_invalid_valid_chars_text(self):
            """Test that a text composed by a mix of invalid and valid chars
               is cleaned correctly.
            """
            self.assertEqual(sluggify('aLmoSt-vAlId sLUg'), 'almost-valid-slug')

We have defined (using tests) what we expect from our :code:`slug.sluggify` function,
now its time to run our test suit and check if our first draft was good enough. To
run the test suit, just run :code:`$ ./test.sh` from the project root directory.

Two of the test should have faild, :code:`test_all_invalid_chars_text` and
:code:`test_mix_invalid_valid_chars_text`. The console output should show a
verbose descrition of why it failed, using that information we can now improve
the sluggify function.

.. code:: python

    # <project_root>/slug.py

    import re

    # This is function is meant to be an example, and is in no way production ready.
    def sluggify(text):
        """Returns a slug based on ``text``"""

        slug = text.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
        slug = re.sub(r'[-]+', '-', slug)

        return slug

Lets run our tests again, :code:`$ ./test.sh`. All green, tests passed, our
sluggify function is ready!

Mocking && Patching
-------------------

Mocking is an esscencial part of testing in python. It allows developers to test
specefic functionality in an insolated way.

Lets create a :code:`class` that represents a :code:`user`. The :code:`User`
will have a name and a property that returns the sluggified version of that name.

.. code:: python

    # <project_root>/user.py

    from slug import sluggify

    class User(object):
        """User representation"""

        def __init__(self, name):
            self.name = name;

        @property
        def name_slug(self):
            return sluggify(self.name)


:code:`User` uses sluggify to return the slug version of its name. When unit testing
the :code:`User` class we shouldn't be testing the :code:`sluggify` functionality,
so how can we fully test :code:`User` without testing :code:`sluggify`? We use
monkey patching, this technique consist on "replacing" the imported modules with
whatever we choose to, that way we can have full control of what our tests are really
testing.

On :code:`python`, just as unit test, mocks are part of the standard. To patch
and mock in our tests we use :code:`unittest.mock`. Lets see an example of it by
testing the :code:`User` class.


.. code:: python

    # <project_root>/tests/test_user.py

    # python standard library for testing
    import unittest

    # python standard library for mocking and patching
    # can't be accesed as unittest.mock so a specific import is
    # needed
    from unittest import mock

    from user import User

    class TestUser(unittest.TestCase):
        """Tests for slug.slugify"""

        # `setUp` is a lifecycle method, its executed before each test on the
        # test suit starts. Its useful for cases like this where we need to have
        # a fresh user with a specific name.
        def setUp(self):
            self.user = User('jon snow')

        # Here we can test deferent aspects of the User class but lets skip
        # right to the `name_slug` test where patching will be used

        # Using the patch decorator, whatever is in the namespace defined in the
        # first argument will be mocked (replaced by a dummy object) and recived
        # it the test as a parameter
        # Notice that the sluggify namespace is from user and not slug, this is
        # not an error, we want to patch sluggify under the user namespace.
        @mock.patch('user.sluggify')
        def test_user_name_slug(self, slug_patch):
            # we can assign the return value of the patched function
            slug_patch.return_value = 'test'

            # let call it and see if the result is what we expect
            self.assertEqual(self.user.name_slug, 'test')

            # now we can assert the sluggify method was actually called
            # and also check that it was called with the correct arguments
            slug_patch.assert_called_with('jon snow')

Using :code:`unittest.mock` we were able to test :code:`user.User` in an isolated
way, now if :code:`slug.sluggify` changes, our user tests won't fail because all
we are testing is that the user is correctly using the sluggify function.

The main benefit of using the isolated test approach is that now, if a test
fails, we will now exactly why, the errors will point to the correct module|class|function
that is not doing what is supposed to. If we weren't patching on the :code:`test_user_name_slug`
test and actually testing that :code:`name_slug` returns the correct slug, if
:code:`slug.sluggify` changes and starts returning inclorrect values, :code:`test_user.py`
and :code:`test_slug.py` both would start failing, making it much harder to figure out
whats the cause of it. In a larger scale project this can mean solving bugs in a
couple of minutes/hours vs solving bugs in a couple of days.


Sources
-------

- https://docs.djangoproject.com/en/1.9/internals/contributing/writing-code/coding-style/
- https://google.github.io/styleguide/pyguide.html
