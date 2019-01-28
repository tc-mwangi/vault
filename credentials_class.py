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