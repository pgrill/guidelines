Table of Contents
-----------------

#. `Styles`_
#. `Tests`_


Styles
------

#. Use four spaces for indentation.
#. Use ``InitialCaps`` for class names (or for factory functions that return classes).
#. Use underscores, not camelCase, for variable, function and method names
   (i.e. ``poll.get_unique_voters()``, not ``poll.getUniqueVoters``).
#. Please conform to the indentation style dictated in the .editorconfig file. 
   We recommend using a text editor with EditorConfig support to avoid indentation 
   and whitespace issues. User the following `.editorconfig file <./files/.editorconfig>`__
   as a base configuration.
#. Follow `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__.
   Use `flake8 <https://pypi.python.org/pypi/flake8>`__ to check for problems in this area.
#. In docstrings, follow `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`__.


Tests
-----

TDD - Unit tests
================

How do we use TDD in Python?

First off, we will start by designing a simple class that will do simple stuff
just by way of example.


.. code:: python


    from django.db import models
    from django.contrib.auth.models import User


    class Activity(models.Model):

        user = models.ForeignKey(User)
        start_date = models.DateField()
        end_date = models.DateField()


        def is_next_week(self):
            return True


This method called :code:`is_next_week`, is a method of activity because as
an example, we had the requirement to list all the activities that were next
week. Now, this is the test class that tests this method and its base scenarios.


.. code:: python

    import datetime

    from django.test import TestCase
    from django.contrib.auth.models import User

    from activities.models import Activity

    class ActivityTestCase(TestCase):

        @classmethod
        def setUp(self):
            super().setUpClass()
            self.user = User.objects.create_user(
                'admin',
                'admin@example.com',
                'examplepass'
            )
            self.this_week = Activity.objects.create(
                user=User.objects.first(),
                start_date=datetime.date.today(),
                end_date=(datetime.date.today() + datetime.timedelta(days=1))
            )

        def test_is_next_week(self):
            self.assertTrue(True)

        def test_is_next_week_passed_next_week(self):
            self.assertTrue(True)

        def test_is_next_week_this_week(self):
            self.assertTrue(True)


The base scenarios are as you can see if it starts in fact next week, if its
this week, or if it is passed next week.

The :code:`setUp` method is a method that we build just because when using
Django, it automatically builds an independent db for the tests which is empty,
so we will have to populate it with something; due to how our models are made,
this is the minimum data we will need to test the method, an activity and a
User.

Now, as this test passes because it is just asserting True to True, we can make
this test case richer.


.. code:: python

    # Rest of the code stays the same.
    def test_is_next_week(self):
        activity = self.this_week
        self.assertTrue(activity.is_next_week())

    # The two other tests change exactly as this one

This test case is richer because its mostly finished, because from now on its
changes will be pretty simple for this example. After making sure this passes by
running the tests, it is time to get to the code, and do it the simplest way we
can. This will be:


.. code:: python

    import datetime

    # (...) rest of code stays the same

    def is_next_week(self):
        # we need to figure out which is the next monday
        next_monday = datetime.date.today()
        while next_monday.weekday() != 0:
            next_monday += datetime.timedelta(1)
        return self.start_date >= next_monday and \
               self.start_date <= (next_monday + datetime.timedelta(7))


The simplest way to see if an activity starts on next week, is by finding out
which is the next monday, and after that, check if the start day is between next
monday and next sunday, if that is true, then the activity starts next week. Now
if you run the test, they will fail, because of the data we entered, and so we
will need to modify the data that we entered in order to make this three test
cases useful, and also the methods to call the correct activity:


.. code:: python

    @classmethod
    def setUp(self):
        super().setUpClass()
        self.user = User.objects.create_user(
            'admin',
            'admin@example.com',
             'examplepass'
        )
        today = datetime.date.today()
        if today.weekday() == 0:
            today += datetime.timedelta(7)
        else:
            today += datetime.timedelta(6)
        self.next_week = Activity.objects.create(
            user=User.objects.first(),
            start_date=today,
            end_date=(today + datetime.timedelta(days=1))
        )
        self.passed_next_week = Activity.objects.create(
            user=User.objects.first(),
            start_date=datetime.date.today() + datetime.timedelta(15),
            end_date=datetime.date.today() + datetime.timedelta(16)
        )
        self.this_week = Activity.objects.create(
            user=User.objects.first(),
            start_date=datetime.date.today(),
            end_date=(datetime.date.today() + datetime.timedelta(days=1))
        )


    def test_is_next_week(self):
        activity = self.next_week
        self.assertTrue(activity.is_next_week())

    def test_is_next_week_passed_next_week(self):
        activity = self.passed_next_week
        self.assertFalse(activity.is_next_week())

    def test_is_next_week_this_week(self):
        activity = self.this_week
        self.assertFalse(activity.is_next_week())


Note: there is still one scenario we are not contemplating, and that would be if
you run this tests on Monday, because it will find next Monday as todays, which
is a validation that follows the same process that we have just described.

This way, the three tests pass and we have ended the round of tdd testing.
What comes next? We assumed that this dates came with the right format, etc. Now
we will need to make sure that happens, but as this is just an example, that is
left for the reader as an exercise.


Sources
-------

- https://docs.djangoproject.com/en/1.9/internals/contributing/writing-code/coding-style/
