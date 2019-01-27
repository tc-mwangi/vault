import unittest # Importing the unittest module
from credentials import User # Importing the user class
# from credentials import Credentials # Importing the credentials class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Loise","Mwangi","tc-mwangi","peppermint92!") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Loise")
        self.assertEqual(self.new_user.last_name,"Mwangi")
        self.assertEqual(self.new_user.user_name,"tc-mwangi")
        self.assertEqual(self.new_user.user_password,"peppermint92!")

    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user  object is saved into
         the user list.
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()    