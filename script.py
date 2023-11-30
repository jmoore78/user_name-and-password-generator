#--------USERNAME GENERATOR--------
"""
The username should be a slice of the first three letters of their first name and the first four letters of their last name. 
If their first name is less than three letters or their last name is less than four letters it should use their entire names.
"""
def username_generator(first_name, last_name):
    username = first_name[:3] + last_name[:4]
    if len(first_name) < 3 or len(last_name) < 4:
        username = first_name + last_name
    return username
print(username_generator("Abe", "Simpson"))
print(username_generator("Abraham", "Sim"))

#--------TEMP PASSWORD GENERATOR--------
"""
The temporary password function should take the input user name and shift all of the letters by one to the right,
so the last letter of the username ends up as the first letter and so forth.
"""
def password_generator(username):
    password = ""
    password = username[-1] + username[:-1] + str(1)
    return password
print(password_generator(username_generator("Abe", "Simpson")))

#--------WORKING THEM TOGETHER--------
def username_generator(first_name, last_name):
    username = first_name[:3] + last_name[:4]
    if len(first_name) < 3 or len(last_name) < 4:
        username = first_name + last_name
    return username

def password_generator(username):
    print(username)
    password = ""
    password = username[-1] + username[:-1] + str(1)
    return password
print(password_generator(username_generator("Abe", "Simpson")))
##################COMBINE THESE TWO AND HAVE THEM TRIGGERED BY A FUNCTION THAT RETRIEVES THE FIRST AND LAST NAMES FROM THE DATABASE#######################