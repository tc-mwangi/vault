# Vault™

Vault is a **secure** password manager that helps store and generate account details for various user accounts.  


## Motivation

On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts. **Vault** will make the tedious process of password retrieval unneccesary.


## Features

- Can copy credentials to the clipboard.
- User can dictate password length. 

## Installation

### Pre-requisites
* [Python 3.7.2](https://www.python.org/)
* IDE of your choice.
* pip
* pyperclip


### Steps

* Run program on terminal:

```
chmod +x run_vault.py
```

* Open the program:

```
./run_vault.py
```

### User Stories.
The application covers the following scenarios:
* create a Vault account with a login username and password.
* store already existing account credentials.
* create new account credentials with a generated password.
* enter a password of their choice.
* view various account credentials/ passwords in the application.
* delete an account that in not needed. 

### BDD
|     | Behaviour    |          Input                  | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | display a menu with navigation options    | [cv], [li] or [ex]     | short-codes: [cv] - create vault [li] - log-in [ex] - exit vault        |
|  2. | if [cv], create account for new user  | first name, last name, username  and password    | input prompts    |
|  3. | if [li] authenticate user      | username and password      | input prompts, confirm successful account creation
     |
|  4. | if [ex]    | [ex]     | exit app, return to terminal    |
|  5. | if successful login, show new navigation options     | [cn], [dc], [cc], [del] and [ex]    |[cn] - Create a New Credential, [dc] - Display Credentials, [cc] - Copy Credential/s, [del] - Delete Credential/s,  [ex] - exit vault" |


## Author

**@top-cat** - *Initial work* - [vault](https://github.com/tc-mwangi/Vault)

## License
MIT © [Vault™]()