import unittest # Importing the unittest module.
from accounts import User # Importing the User class
from accounts import Credentials # Importing the Credentials class


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

# self,first_name,last_name,user_name, user_password)

    def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected.
		'''
		self.new_user = User("Loise", "Mwangi", "tcmwangi", "peppermint")
		self.new_user.save_user()
		user2 = User("Ian", "Kabugi", "iankabugi", "laptop")
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.user_password == user2.password:
				this_user = user.first_name
		return this_user

		self.assertEqual(this_user, Credentials.check_user(user2.password,user2.first_name))

