Table of Contents
=================

1. `Books`_
2. `Files`_
3. `Templates`_
4. `Signals`_


Books
=====

#. `Django Two Scoops <http://twoscoopspress.org/>`__


Files
=====

.. code:: yaml

    py: lowercase_with_underscores.py
    html: lowercase_with_underscores.html
    javascript: lowercase-with-dashes.js
    images: lowercase-with-dashes.*
    css: lowercase-with-dashes.*
    scss: lowercase-with-dashes.*
    scss (partials): _lowercase-with-dashes.*


Templates
=========

-  Name blocks with lowercase and underscores.

.. code:: html

    {% block lowercase_with_underscores %}
    {% endbblock lowercase_with_underscore %}

-  If the block/endblock is inline you should avoid the name on the
   endblock.

-  In endblocks, add the name of the block they close.

.. code:: html

    {% block foo_bar %}
        ...
    {% endblock foo_bar %}

-  Indent everything within template tags.

.. code:: html

    {% block foo_bar %}
        <html-tag></html-tag>
        {% if foo %}
            <html-tag></html-tag>
        {% else %}
            <html-tag></html-tag>
        {% endif %}
    {% endblock foo_bar %}


Signals
=======

.. code:: bash

    app/signals/__init__.py # Define new signals
    app/signals/handlers.py # Define handlers

.. code:: python

    from django.apps import AppConfig as BaseAppConfig


    class AppConfig(BaseAppConfig):

        ...

        def ready(self):


Tests
=====

Introduction
------------

First off, suppose you were required to create an app that should register user
activities and then show if the activity was done on the current week.

In order to do that you decide to create a new model. Where should you start?
well you could start by creating the activity class, defining its fields and
methods, documenting it, integrate it with the rest of the app, clicking around to
make sure everything works and then write tests as an after thought.

There are a couple of problems with that workflow, the main one (related to testing) is that creating
the tests after the functionality will make you adapt your tests to the functionality
and not the other way around, so the tests, instead of describing the requirements
will describe the already implemented functionality (which can be wrong).

Also, by writing tests firsts, you'll have a clear definition of the required public
interface, the client requirements and a clear ending point of the development process.
Once your test suit passes, you've successfully implemented the requirements, of course
this doesn't necessarily means you are done, refactor is a key element in the development
of any kind of software.

Project structure and configuration
-----------------------------------


When creating an app, by default, django creates a test.py file on the app
directory. We recommend deleting that file and creating a package in the same
directory named tests. Inside it, create test_*.py files to test specific parts
of the app (test_models.py, test_views.py, etc). Django will be able to find those
tests anyway and it will be easier to maintain afterwards.

We also like to keep a specific configuration for testing that depends on the
environment, so if the environment variable TEST is true then all the project
settings reflect it.

If the project has tests that interact with the database, we configure our test
database to use the same drivers as the production database so we can mimic the
production environment as much as we can.


TDD - Unit tests
----------------

How do we use TDD in Django?

We will start by defining the tests for the requirements defined on the introduction.

.. code:: python

    import datetime

    from django.test import TestCase
    from django.contrib.auth.models import User

    # The Activity model does not exists yet, but by creating
    # this test we already made the decision on where it should be defined
    from activities.models import Activity
    from users.models import User

    # All tests that interact with the database
    # should extend django.test.TestCase, this makes sure
    # all your tests run inside a transaction.
    # TestCase extends unittest.TestCase so all the standard python assertion
    # helpers are available on the test suit
    class ActivityTestCase(TestCase):

        # This method is called once before running this
        # test suit, so it should be used to configure
        # values that are used across all the test suit
        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.user = User.objects.create_user(
                'admin',
                'admin@example.com',
                'examplepass'
            )

        # Test names should describe what the test is doing,
        # also, its important that the name starts with test_*
        # this is what tells django that it should be executed
        # when running the test suit
        def test_is_current_week_with_current_week(self):

            # The activity model does not exists but here we've
            # defined what fields should be required
            # on the activity
            activity = Activity.objects.create(
                user=cls.user,
                done_at=datetime.date.today(),
            )

            # And by asserting its functionality we already
            # defined the method signature and its expected
            # functionality
            self.assertTrue(activity.is_current_week())

        # Its important to test failing cases as well
        def test_is_current_week_with_next_week(self):
            activity = Activity.objects.create(
                user=cls.user,
                done_at=datetime.date.today() + datetime.timedelta(days=7),
            )
            self.assertFalse(activity.is_current_week())

        def test_is_current_week_with_previous_week(self):
            activity = Activity.objects.create(
                user=cls.user,
                done_at=datetime.date.today() - datetime.timedelta(days=7),
            )
            self.assertFalse(activity.is_current_week())

Now we have to write the Activity class, or else the test will definitely fail.
We already defined the Activity on the test, so this process should be
really straightforward.

We'll start by implementing the bare minimum so that we can run the tests.

.. code:: python


    from django.db import models
    from django.contrib.auth.models import User


    class Activity(models.Model):

        user = models.ForeignKey(User)
        done_at = models.DateField()

        # We know how the method should be named and
        # that it should return a boolean so thats all
        # we implement for now
        def is_current_week(self):
            return True

Now we can run our tests. This is done by running :code:`$ ./manage.py test` on
the terminal. In this case test will fail, but thats okay, the development process
should be: run test - fail tests - refactor - success test - refactor - run test
and continue the cycle until you are satisfied with the implementation. If test
exists, you'll be able to refactor your implementation with the assurance that
you are always complying with the requirements.

Now lets update the Activity class so out test don't fail.


.. code:: python

    # (...) The rest of code stays the same, we only need to udpdate
    # is_current_week

    def is_current_week(self):
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        sunday = today + datetime.timedelta(days=6)

        return monday <= self.done_at <= sunday

Run tests with :code:`$ ./manage.py tests` and tests should be successful! Now we
can be sure we finished with the original requirements and move on to the next
feature that needs to be implemented.

So we finish out first round of tdd testing.
What comes next? We assumed all dates where correctly formatted and that is_current_week
never unexpectedly failed. We should be testing those edge cases as well,
but as this is just an example, that is left for the reader as an exercise.

If you want to see how we do tests, please click here_.

.. _here: https://github.com/sophilabs/guidelines/tree/master/python#tdd-unit-tests
