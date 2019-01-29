from user_class import User

class Credentials:
    
    """
    Class that creates details for online accounts, saves details and generates passwords/allows user passwords.
    """

    credentials_list = [] #
    user_credentials_list = [] #

    @classmethod
    def check_user(cls, user_name, user_password):
        '''
        method checks whether user is registered/is in the users_list.
        '''
        this_user = "" #empty string
        for user in User.users_list:
            if(user.user_name == user_name and user.user_password == user_password):
                this_user = user.first_name
        return this_user





