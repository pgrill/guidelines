Django's Guidelines
-------------------

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

TDD
^^^

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

Also, by writing tests first, you'll have a clear definition of the required public
interface, the client requirements and a clear ending point of the development process.
Once your test suit passes, you've successfully implemented the requirements, of course
this doesn't necessarily means you are done, refactor is a key element in the development
of any kind of software.

Project structure and configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Folder structure**

When creating an app, by default, django creates a test.py file on the app
directory. We recommend deleting that file and creating a package in the same
directory named tests. Inside it, create test_*.py files to test specific parts
of the app (test_models.py, test_views.py, etc). Django will be able to find those
tests anyway and it will be easier to maintain afterwards.


**Test Data**

As Django Two Scoops suggests, relying on fixtures could be problematic. They are hard to maintain,
especially as it can be difficult to identify during the JSON load process where your JSON files
are either broken or a subtly inaccurate representation of the database.

To create initial data we use `Factory Boy <https://factoryboy.readthedocs.io/>`__.

**Configurations**

We also like to keep a specific configuration for testing that depends on the
environment, so if the environment variable TEST is true then all the project
settings reflect it.

If the project has tests that interact with the database, we configure our test
database to use the same drivers as the production database so we can mimic the
production environment as much as we can.

**Coverage**

Coverage is good metric to know how much of your code is being checked by your
tests, we use `coverage.py <http://coverage.readthedocs.io/en/latest/>`__ for this.
It has seemingness integration with django, all we need to do is run
:code:`coverage run --source='.' manage.py test` when running tests. On most cases
that command won't be enough for the project necessities though, so we end up creating
a :code:`test.sh` file to set all environment variables and configurations
and run test. As an example:

.. code:: bash

    #!/bin/bash

    WARNINGS=0 TEST=YES coverage run --source=. manage.py test --noinput "$@"

    if [ "$?" -eq '0' ]; then
      coverage html
    fi


Unit tests
^^^^^^^^^^

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

        # setUpClass is called once before running this
        # test suit, so it should be used to configure
        # values that are used across all the test suit.
        # From Django 1.8 onwards, setUpTestData should
        # be used instead as it is specifically for that
        # purpose.

        # For Django 1.7 and lower
        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.user = User.objects.create_user(
                'admin',
                'admin@example.com',
                'examplepass'
            )

        # For Django 1.8 and higher
        @classmethod
        def setUpTestData(cls):
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

Functional Tests
^^^^^^^^^^^^^^^^

The main purpose of functional tests is testing features. In django features could mean views,
business logic or any other workflow involving several parts of the application.

    **Monkey patching and Inverse of control**

    In Python, as a dynamic language, its not common to use a DIC or use
    inverse of control patterns when designing the application, so in most cases
    there is strong coupling between classes. This is particularly common on
    django views.

    That being said, inversion of control as a way of avoiding strong coupling
    will make test a lot easier so it should be applied whenever possible.

Continuing with the requirements defined on the introduction we should be able
to show the activities of a user and if they where done on the current week.
As we did with the unit test, we can benefit from writing the tests first.

.. code:: python

    import datetime
    from django.test import TestCase, Client
    from django.contrib.auth.models import User
    from activities.models import Activity
    from users.models import User

    class ActivityTestCase(TestCase):

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            cls.user = User.objects.create_user(
                'admin',
                'admin@example.com',
                'examplepass'
            )

        # We use a new client for each test
        def setUp(self):
            # Client is a django helper for making requests
            # to out app, it supports all request types (GET, POST, DELETE, etc..)
            self.client = Client()

        def test_incorrect_url_returns_404(self):
            # Its a good practice to hardcode urls on tests.
            # Users can bookmarks urls, so if a url change in our
            # project, we should add a permanent redirect from the old
            # url to the new one.
            response = self.client.get('/user/0/activities')

            # User with id 0 does not exist. We define in the test that
            # if no user is found, the response code should be 404
            self.assertEqual(response.status_code, 404)

        def test_user_with_no_activities(self):
            response = self.client.get(
              '/user/{}/activities'.format(self.user.id)
            )

            # We define whats the status code when the user exists
            self.assertEqual(response.status_code, 200)

            # We can assert the body of the response with contains,
            # we could also test the context passed into the response
            # with resonse.context.
            # We define what the body should contain if the user
            # has no activities
            self.assertContains(response, 'No activities')

        def test_user_with_old_activities(self):
            response = self.client.get(
                '/user/{}/activities'.format(self.user.id)
            )

            activity = Activity.objects.create(
                user=self.user,
                done_at=datetime.datetime.now() - datetime.timedelta(days=7)
            )

            self.assertEqual(response.status_code, 200)

            # Defines what the body should contain in case there are any
            # old activities
            self.assertContainer(response, str(activity.id))

        def test_user_with_new_activities(self):
            response = self.client.get(
                '/user/{}/activities'.format(self.user.id)
            )

            activity = Activity.objects.create(
                user=self.user,
                done_at=datetime.datetime.now()
            )

            self.assertEqual(response.status_code, 200)

            # Defines what the body should contain in case there is any
            # new activity
            self.assertContaines(
                response,
                '{} was done this week!'.format(activity.id)
            )

Now that we defined how our view should behave we can start implementing it,
we run test the same way we did for unittest :code:`./manage.py test`.

Implementing the view should be easy now, we have all major steps defined.

.. code:: python

    # view.py

    from django.views.generic.detail import DetailView
    from accounts.models import User

    class UserDetailView(DetailView):
        template_name = "user.html"
        model = User

    # urls.py

    urlpatterns = [
      url(r'^users/(?P<user_id>[0-9]+)/$',
          UserDetailView.as_view(), name='user-detail'),
    ]

.. code:: html

    # user.html

    {% for activity in object.activities %}
      {% if activity.is_current_week %}
        <p>{activity.id} was done this week!</p>
      {% else %}
        <p>{activity.id}</p>
      {% endif %}
    {% empty %}
      <p>No activities</p>
    {% endfor %}

Because we had all the tests before coding the actual views, it makes it easier to
implement, we know what type of views we should use (DetailView), we know we
have to show something even if :code:`objects.activities` is empty and we know
how the url should look. Now we can do progressive enhancements with confidence,
knowing that if we mess up, the tests will let us know. Next we could add
styles, javascript, more context information and as long as the test keep giving
us the okay, we are complying to the requirements and our app works!

Acceptance Tests
^^^^^^^^^^^^^^^^

While unit and functional tests are classified as white box tests, acceptance tests are considered black box tests.
They are used to determine if the requirements of the specifications are met.

**Selenium**

Suppose the app should only display the user activities after clicking a button
on the page. This will use javascript to make an ajax call to bring the activities
and then insert them in the DOM. We can't test that with out current stack as
it does not runs javascript.

Enter `Selenium <http://www.seleniumhq.org/>`__ a web browser automation.

Testing with selenium in django is extremely easy.

First, our tests should extend :code:`django.contrib.staticfiles.testing.StaticLiveServerTestCase`.
StaticLiveServerTestCase launches a live django server in the background (running our app)
and serves the static files to it.

Here is how the selenium test would look like:

.. code:: python

    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.wait import WebDriverWait


    class UserActivitiesTest(StaticLiveServerTestCase):
        def setUp(self):
          # (...) test setup, creating user and context

          # First we load the selenium driver, its responsable of controlling
          # the browser.
          # We like using a chrome webdriver as its our goto browser
          self.selenium = webdriver.Chrome(<path_to_driver>)
          self.selenium.maximize_window()
          super(GenerateReportTest, self).setUp()

        def tearDown(self):
            # Its important to close the selenium session
            # once out test are done
            self.selenium.quit()
            super(GenerateReportTest, self).tearDown()

        def test_async_user_activities(self):
            # Load the page into the browser
            self.selenium.get(
                '{}{}'.format(self.live_server_url, '/user/1/activities')
            )

            # We can select DOM elements and interact with them
            activity_button = self.selenium.find_element_by_id("activity-button")
            activity_button.click()

            # We wait for the activities maximum (acceptable) time
            # and set the expected condition, if the time is reached and
            # the condition evaluates to false, the test will fail.
            WebDriverWait(self.selenium, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.CLASS_NAME, "user-activity")
                )
            )

The above test, will check a couple of things. It will test that there is a button
with the id :code:`activity-button`, it will check that when clicked the user should
see an element with the class :code:`user-activity` and it will test that the delay
between the click and the DOM update takes less that 10 seconds.

So we are effectively testing the user experience. There is one big downside for
this kind of test, if the html markup changes, the test will fail. Depending on
the project, this can be a good thing or a bad thing. If the project is constantly
redesigning its identity, the effort of maintaining this test is probably not worth
it, but if the project has well defined style guidelines and its important for the
application to comply to them, then the development process could really benefit
from having this tests.

The are different cases where its important (or mandatory) to test you website
javascript and ux, to name a few:

- SPA applications
- Partial content loading
- Real time applications
- Strong Identity sites
- Short loading time requirement

For all those cases we need to be able to load the web page and simulate the user
interaction with it, that way, we can make sure that the user experience in our
site is the one that is expected. After all, the user experience is what gives
value to our site, it would be foolish not to test it.
