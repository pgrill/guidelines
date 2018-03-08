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