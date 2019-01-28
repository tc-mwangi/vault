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
def check_user(user_name,user_password):
	'''
	function checks to see if a user is registered in the user list.
	'''
	checking_user = Credentials.check_user(user_name,user_password)
	return checking_user

def main():
    print("\n")
    print("Welcome to Vault, your reliable account/password manager.")
    print("\n")
    while True:
        print("What would you like to do today?" )
        print("\n")
        print(" [cv] - create vault account, [li] - log-in,  [ex] - exit vault")
        print("\n")
        short_code = input("Enter short code: ").lower()

        if short_code == "cv":
            #ask for details
            print("Enter the following details:")
            print ("First name ....")
            first_name = input()
            print ("Last name ....")
            last_name = input()
            print ("User name ....")
            user_name = input()
            print ("Password ....")
            user_password = input()

            #save new user
            save_user(create_user(first_name, last_name, user_name, user_password))
            print(f'New vault Account Details: {first_name} {last_name} {user_name} using password: "{user_password}"')

        elif short_code == "li":
            print ("Username ....")
            user_name = input()
            print ("Password ....")
            user_password = input()

            #verify user
            check_user

            # user_exists = verify_user(user_name,password)
			# if user_exists == user_name:
			# 	print(" ")
			# 	print(f'Welcome {user_name}. Please choose an option to continue.')
			# 	print(' ')
			# 	while True:
			# 		print("-"*60)
			# 		print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
			# 		short_code = input('Enter a choice: ').lower().strip()
			# 		print("-"*60)
			# 		if short_code == 'ex':
			# 			print(" ")
			# 			print(f'Goodbye {user_name}')
			# 			break
			# 		elif short_code == 'cc':
			# 			print(' ')
			# 			print('Enter your credential details:')
			# 			site_name = input('Enter the site\'s name- ').strip()
			# 			account_name = input('Enter your account\'s name - ').strip()

        
            

        elif short_code == "ex":
            print("Good bye!")
            break
        else:
            print("Please use the short codes provided !")

        

        

            
           
			



        # elif short_code == "li":
        #     #ask for login details
        #     print("Vault Login")
        #     print("\n")
        #     print ("Username ....")
        #     user_name = input()
        #     print ("Password ....")
        #     user_password = input()
            
            
if __name__ == '__main__':

    main()
            
       


        

  


