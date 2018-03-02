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
        self.assertContains(
            response,
            '{} was done this week!'.format(activity.id)
        )