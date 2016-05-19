Python
======

-**`⬅ back to index <./>`__**

Styles
------

-  Use ``flake8`` and ``iosort``

-**`⬅ back to index <./>`__**


TDD - Unit tests
-----

How do we use TDD in Python?

First off, we will start by designing a simple class that will do simple stuff
just in form of example.


.. code:: python


    from django.db import models
    from django.contrib.auth.models import User


    class Activity(models.Model):
        user = models.ForeignKey(User)
        start_date = models.DateField()
        end_date = models.DateField()


        def is_next_week(self):
            return True


This method called is_next_week, is a method of activity because as an example,
we had the requirement to list all the activities that were next week. Now, this
is the test class that tests this method and its base scenarios.


.. code:: python

    import datetime

    from django.test import TestCase
    from django.contrib.auth.models import User

    from activities.models import Activity

    # Create your tests here.


    class ActivityTestCase(TestCase):
        def setUp(self):
            User.objects.create_user('admin', 'admin@example.com', 'examplepass')
            Activity.objects.create(
                user=User.objects.first(),
                start_date=datetime.date.today(),
                end_date=(datetime.date.today() + datetime.timedelta(days=1))
            )

        def test_is_next_week(self):
            self.assertTrue(True)

        def test_is_next_week_passed_next_week(self):
            self.assertTrue(True)

        def test_is_next_week_today(self):
            self.assertTrue(True)


The base scenarios are as you can see if it starts in fact next week, if its
this week, or if it is passed next week.

The setUp method is a method that we build just because when using Django, it
automatically builds an independent db for the tests which is empty, so we will
have to populate it with something; due to how our models are made, this is the
minimum data we will need to test the method, an activity and a User.

Now, as this test passes because it is just asserting True to True, we can make
this test case richer.


.. code:: python

    # Rest of the code stays the same.
    def test_is_next_week(self):
        activity = Activity.objects.first()
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


    def setUp(self):
            User.objects.create_user('admin', 'admin@example.com', 'examplepass')
            today = datetime.date.today()
            if today.weekday() == 0:
                today += datetime.timedelta(7)
            else:
                today += datetime.timedelta(6)
            Activity.objects.create(
                user=User.objects.first(),
                start_date=today,
                end_date=(today + datetime.timedelta(days=1))
            )
            Activity.objects.create(
                user=User.objects.first(),
                start_date=datetime.date.today() + datetime.timedelta(15),
                end_date=datetime.date.today() + datetime.timedelta(16)
            )
            Activity.objects.create(
                user=User.objects.first(),
                start_date=datetime.date.today(),
                end_date=(datetime.date.today() + datetime.timedelta(days=1))
            )


        def test_is_next_week(self):
            activity = Activity.objects.get(pk=1)
            self.assertTrue(activity.is_next_week())

        def test_is_next_week_passed_next_week(self):
            activity = Activity.objects.get(pk=2)
            self.assertFalse(activity.is_next_week())

        def test_is_next_week_today(self):
            activity = Activity.objects.get(pk=3)
            self.assertFalse(activity.is_next_week())


This way, the three tests pass and we have ended the round of tdd testing.
What comes next? We assumed that this dates came with the right format, etc. Now
we will need to make sure that happens, but as this is just an example, that is
left for the reader as an exercise.
