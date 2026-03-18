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