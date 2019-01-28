# !/user/bin/env python3.7
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
	verifying_user = Credentials.check_user(user_name,user_password)
	return verifying_user

def main():
    print("\n")
    print("Welcome to Vault.")
    while True:
        print("\n")
        print("What would you like to do today?" )
        print("\n")
        print(" Navigation short codes: \n [cv] - create vault account, \n [li] - log-in, \n [ex] - exit vault")
        print("\n")
        short_code = input("Enter short code: ").lower()

        if short_code == "ex":
            break

        elif short_code == "cv":
            print("\n")
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
            
            #next, log in user
        elif short_code == "li":
            print ("Enter your login details")
            print ("Username ....")
            user_name = input()
            print ("Password ....")
            user_password = input()

            #verify user
            user_in_list = check_user(user_name, user_password)

            if user_in_list == user_name:
                print("\n")
                print(f"Welcome {first_name} {last_name}. What would you like to do?")
                print(" ")
                while True:
                    print("[cc] - Create a New Credential, \n [dc] - Display Credentials, \n [del] - Delete Credential/s, \n [ex] - exit vault")

                short_code = input("Enter short code: ").lower()
                print("\n")

                if short_code == "ex":
                    print("\n")
                    print(f"Bye {first_name} {last_name}.")

            else:
                  print("\n")
                  print("User doesn't exist! Would you like to: ")
                  print("[cv] - Create Vault Account or [ta] - Try Again")
                  print("\n")
                  short_code = input("Enter short code: ").lower()

                

            


              
           
        elif short_code == "ex":
            print("Good bye!")
            break
        else:
            print("Please use the short codes provided !")    

        
            

            # print("What would you like to do next?")
            # print("[cc] - Create a new Credential, [dc] - Display Credentials")

			 	
            

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

        
                    
            
if __name__ == '__main__':

    main()
            
       


        

  


