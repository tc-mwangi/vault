#!/user/bin/env python3.7
#imports
from user_class import User
from credentials_class import Credentials
import pyperclip


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

# create a new credential function.
def create_credentials(account_name, account_user_name, account_user_email, account_user_password):
	'''
	Function to create a new credential
	'''
	new_credential = Credentials(account_name, account_user_name , account_user_email, account_user_password)
	return new_credential

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
    print("What would you like to do today?")
    print("\n")
    while True:
        print(" Find your way around with thes short-codes: \n [cv] - create vault account \n [li] - log-in \n [ex] - exit vault")
        print("\n")
        short_code = input("Enter short code: ").lower()
    
        if short_code == "cv":
            print("\n")
            #ask for details
            print("Enter the following details:")
            print ("First name...?")
            first_name = input()
            print ("Last name...?")
            last_name = input()
            print ("User name...?")
            user_name = input()
            print ("Password...?")
            user_password = input()

            #save new user details
            save_user(create_user(first_name,last_name, user_name, user_password))

            #confirm save
            print(f"Successful Sign-up {first_name} {last_name}")
             
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
                print(f"Welcome {user_name}. What would you like to do?")
                print(" ")
                while True:
                    print("[cn] - Create a New Credential, \n [dc] - Display Credentials, \n [cc] - Copy Credential/s, \n [del] - Delete Credential/s, \n [ex] - exit vault")
                    short_code = input("Enter short code: ").lower()
                    print("\n")
                    if short_code == "ex":
                        print("\n")
                        print(f"Bye {first_name} {last_name}.")

                    elif short_code == "cn":
                        print("Enter your online accont credentials")
                        print ("Account name...? eg. facebook, twitter, instagram")
                        account_name = input().strip
                        print("Account username...?")
                        account_user_name = input()
                        print("Account email...?")
                        account_user_email = input()
                        print("Account password...?")
                        account_user_password = input()



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

        
        
                        
            
if __name__ == '__main__':

    main()
            
       


        

  


