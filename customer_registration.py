#This is the Email and username validator
def email_validator(email:str)-> str:
    validator = len(email)
    if validator < 10:
        print("Is not a valid email, a valid email has a minimum of 10 letters")
        email = input("Enter a valid email: ")
        return email_validator(email)
        
    if "@" not in email: 
        print("Invalid Email, a valid one has an '@' on it!")
        email = input("Enter a valid email: ")
        return email_validator(email)

    if "." not in email: 
        print("Invalid Email, doesn't has a dot")
        email = input("Enter a valid email: ")
        return email_validator(email)
    return email

def name_validator(name: str):
    if name.strip() == "":
        print("Name cannot be a empty. Try again!")
        name = input("Enter a valid name: ")
        return name_validator(name)
    return name

#This is the user_dict creation
def create_user(user_name: str, user_email: str) -> dict:
    user = {"username": user_name, "email": user_email}
    return user
    
#This is the function to add the user_dict to the database_dict
def add_to_db(user: dict, db: dict) -> dict:
    new_id = 0
    try:
        last_id = next(reversed(db))
        new_id +=  last_id + 1
    except StopIteration:
        new_id = 1 #Based on the requirement this is going to be 0 or 1. 
    db[new_id] = user
    return db


customers_db = {}

print(customers_db)

name = input("Enter a new customer name: ")
name_validated = name_validator(name)

email = input("Enter a new customer email: ")
email_validated = email_validator(email)

new_user = create_user(name_validated, email_validated)
customers_db = add_to_db(new_user, customers_db)
print(customers_db)


