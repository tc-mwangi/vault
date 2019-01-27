class User:
    """
    Class that creates vault account for users.
    """

    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,user_name, user_password):

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_password = user_password

class Credentials:
    """
    Class that creates account details and generates random passwords.
    """

    credential_list = [] # Empty credentials' list
    user_credential_list = []

    def __init__(self,user_name, user_password):

        # instance variables
        self.user_name = user_name
        self.user_password = user_password