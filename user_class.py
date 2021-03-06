class User:
    """
    Class that creates new vault accounts for users.
    """

    users_list = [] # directory of all registered users
    def __init__(self,first_name,last_name,user_name, user_password):
        
        '''
        method lists properties that each user object will have to create a new account.
        '''

        # user instance variables.
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_password = user_password
 
    def save_user(self):

        '''
        function saves new vault users to user_list.
        '''

        User.users_list.append(self)

    