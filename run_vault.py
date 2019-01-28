#imports
from user_class import User
from credentials_class import Credentials
# import pyperclip


# create user function
def create_user(first_name, last_name, user_name, user_password):
	'''
	function creates new vault account.
	'''
	new_user = User(first_name, last_name, user_name, user_password)
	return new_user


# save user function
def save_user(user):
	'''
	function saves new vault user.
	'''
	User.save_user(user)

# verify user before they can proceed to create credentials.
def check_user(first_name,password):
	'''
	function checks to see if a user is registered in the user list.
	'''
	checking_user = Credentials.check_user(first_name,password)
	return checking_user

def main():
    
    print("Welcome to Vault, your reliable account/password manager.")
    while True:
        print("What would you like to do today?" )
        print(" li - log-in, ca - create vault account, ex - exit vault")
        short_code = input("enter short code").lower()

        if short_code == "ca":
            #ask for login details
            print("Enter the following details:")
            print ("First name ....")
            first_name = input()
            print ("Last name ....")
            last_name = input()
            print ("User name ....")
            user_name = input()
            print ("Password ....")
            user_password = input()
            

if __name__ == '__main__':

    main()
            
       


        

  


