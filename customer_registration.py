def email_validator(email:str)-> str:
    validator = len(email)
    if validator < 10:
        print("Is not a valid email, a valid email has a minimum of 10 letters")
        return None
    if "@" not in email: 
        print("Invalid Email, a valid one has an '@' on it!")
        return None
    if "." not in email: 
        print("Invalid Email, doesn't has a dot")
        return None
    return email

def create_user(user_name: str, user_email: str) -> dict:
    if user_name.strip() == "":
        print("Name cannot be a empty. Try again!")
        return None
    user = {"username": user_name, "email": user_email}
    return user
    

def add_to_db(user: dict, db: dict) -> dict:
    new_id = 0
    try:
        last_id = next(reversed(db))
        new_id +=  last_id + 1
    except StopIteration:
        new_id = 1 #Based on the requirement this is going to be 0 or 1. 
    db[new_id] = user
    return db


user_database = {}

name = input("enter name: ")
email = input("enter email: ")

user_1 = create_user(name, email)

print(add_to_db(user_1, user_database))

name = input("enter name: ")
email = input("enter email: ")

user_2 = create_user(name, email)

print(add_to_db(user_2, user_database))


#Example
#This is how the product_db has to look
false_db = {
    1: {
    'username': 'Juan', 
    'email': 'juanito@gmail.com'}, 
    2: {'username': 'Pepito Perez', 
        'email': 'pepitope@gmail.com'}
        }