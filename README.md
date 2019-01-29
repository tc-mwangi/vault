<!-- # Vault™

Vault is a **secure** password manager that helps store and generate account details for various user accounts.  

## Motivation

On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts. **Vault** will make the tedious process of password retrieval unneccesary.

## Tech/framework used

- [Python 3.7.2](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/) -->

<!-- 
## Features
- Can copy credentials to the clipboard.
- User can dictate password length. -->

<!-- ## Installation

### Pre-requisites
- pip


Steps

Run program on terminal:

```
chmod +x run_vault.py
```

Open the program:

```
./run_vault.py
```

## BDD

### User Stories.
The application covers the following scenarios:
* create a Vault account with a login username and password.
* store already existing account credentials.
* create new account credentials with a generated password.
* enter a password of their choice.
* view various account credentials/ passwords in the application.
* delete an account that in not needed. 


|     | Behaviour    |          Input                 | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | display a menu with navigation options    | login username & password      | git status    |
|  2. | store existing account details   | git status     | git status    |
|  3. | create new account details      | git diff       | git diff      |
|  4. | generate passwords for new accounts   | git status     | git status    |
|  5. | enable user-generated passwords for new accounts  | git status     | git status    |
|  6. | view list of account details/passwords| git diff       | git diff      |

## Contribute

Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus. -->

<!-- ## Credits
* one
* two
* three -->

<!-- ## Author

**@top-cat** - *Initial work* - [vault](https://github.com/tc-mwangi/Vault)

## License
MIT © [Vault™]() -->

# Vault™

Vault is a **secure** password manager that helps store and generate account details for various user accounts.  

## Motivation

On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts. **Vault** will make the tedious process of password retrieval unneccesary.

## Tech/framework used

- [Python 3.7.2](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/)

<!-- 
## Features
- Can copy credentials to the clipboard.
- User can dictate password length. -->

## Installation

### Pre-requisites
* [Python 3.7.2](https://www.python.org/)
* pip
* paperclip


Steps

Run program on terminal:

```
chmod +x run_vault.py
```

Open the program:

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
|  5. | if successful login,      | git status    | |
|  6. | view list of account details/passwords| git diff       | git diff      |

## Author

**@top-cat** - *Initial work* - [vault](https://github.com/tc-mwangi/Vault)

## License
MIT © [Vault™]()