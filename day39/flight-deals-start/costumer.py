import requests
f_name = input("What is your first name:")
l_name = input("What is your last name:")

is_equal = False
while not is_equal:
    email_id = input("What is your e-mail id:")
    conf_email_id = input("Confirm your e-mail id:")
    if email_id == conf_email_id:
        is_equal = True
    else:
        print("Please retry")    


if email_id == conf_email_id:
    body = {
    "user":{
        "firstName":f_name,
        "lastName":l_name,
        "email":email_id
        }
    }
    response = requests.post("https://api.sheety.co/85af671b56f941cac2a6be9a342a0f9f/copyOfFlightDeals/users", json=body)
    
    
