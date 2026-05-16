import json

d = "data.json"

try:
    with open(d, 'r') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty dict if file doesn't exist or is corrupted
        data = {}


def get_user_info(user_id = None) -> dict | None:
    try:
        return data[user_id]
    except:
        print("The User Not Found.")
        return None
    
def update_user(user_id = None,user_data = None):
    if user_id != None and user_data != None:
        data[user_id] = user_data
        # print(data)
        with open(d,"w") as f:
            json.dump(data,f,indent=4)            
        