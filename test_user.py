import unittest # Importing the unittest module.
from accounts import User # Importing the User class
from accounts import Credentials # Importing the Credentials class

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

    # test1-create user account
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"loise")
        self.assertEqual(self.new_user.last_name,"mwangi")
        self.assertEqual(self.new_user.user_name,"tcmwangi")
        self.assertEqual(self.new_user.user_password,"peppermint")

    # test2-save user
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_list.
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    # test3-save multiple users
    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run.
        '''
        User.user_list = []
        
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","tc-mwangi","peppermint92!") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

     # test4-delete user account
    # def delete_user(self):
    #     '''
    #     test case to remove saved user acoount.
    #     '''
    #     User.user_list.remove(self)

       
if __name__ == '__main__':
    unittest.main()    