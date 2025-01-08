
# [a-bA-B\w]+        #Username
# \b[a-zA-Z\W\w]+  #password

import re
class InvalidusernameError(Exception):
    pass
class InvalidpasswordError(Exception):
    pass
username=0
password=0

def accept_input():
    global username
    global password
username=int(input("Enter the Username : "))
password=int(input("Enter the password : "))

def varify():
    if username==username and password==password:
        print("Login successfull!!")
    else:
        raise InvalidusernameError("please try to provide valid credentilas")
    
    try:
        





