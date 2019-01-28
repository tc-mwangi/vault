class User:
    """
    Class that creates new vault accounts for users.
    """

    user_list = [] # directory of all registered users
 
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
    Class that creates details for online accounts and generates passwords/allows user passwords.
    """

    credentials_list = [] #
    user_credentials_list = [] #

    @classmethod
    def find_by_user_name(cls, user_name, user_password):

        '''
        method that checks whether user has a vault account i.e is in the user_list.
        '''



        




    # def __init__(self, email, full_name, username, password):

    #     # instance variables... Test with instagram
    #     self.email = email
    #     self.user_full_name = full_name
    #     self.user_name = username
    #     self.user_password = password