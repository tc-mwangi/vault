class User:
    """
    Class that creates new vault accounts for users.
    """

    user_list = [] # class variable: can be accessed by all instances.
 
    def save_user(self):

        '''
        save_user method saves new vault users to user_list.
        '''

        User.user_list.append(self)

    def __init__(self,first_name,last_name,user_name, user_password):
        
        '''
        method lists properties that each user object will have to create a new account.
        '''

        # user instance variables.
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_password = user_password

class Credentials:
    """
    Class that creates details for various online accounts and generates passwords/allows user passwords.
    """

    credential_list = [] #
    user_credential_list = [] #

    def __init__(self,user_name, user_password):

        # instance variables
        self.user_name = user_name
        self.user_password = user_password