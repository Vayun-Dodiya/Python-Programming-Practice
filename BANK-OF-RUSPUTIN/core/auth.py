import core.storage as st

def Login_check(user_id = None,PIN = None):

    user_data = st.get_user_info(user_id)
    
    if user_data != None and user_data["Status"] == "Active":
    
        if PIN == None:
            PIN = input("Enter PIN : ")

        for i in range(2,0,-1):
            
            if user_data["PIN"] == PIN and len(PIN) == 4:
                print("Login Successful!")
                return (user_data,True)
            else:
                print("Invalid PIN." if user_data["PIN"] != PIN else "Invalid Pin Length.")
                PIN = input(f"Enter The Pin ({i} attempts remaining):")
        else:
            print("0 attempts Left!\nYour Account is Locked.")
            user_data["Activity"] = "LOCKED"
            st.update_user(user_id,user_data)
    
    else:
    
        if user_data == None:pass
    
        elif user_data["Activity"] == "LOCKED":
            print("\nCannot Login!\nYour Account Is Currently Locked For Some Reasons.")
    
        return (None,False)
    

def unlock(user_id = None, admin_pin = None, SeQu = None):
    user_Data = st.get_user_info(user_id)
    if user_Data["Activity"] == "LOCKED":
        if admin_pin != None and admin_pin != 0:
            if admin_pin == int(user_Data["Admin Pin"]):
                user_Data["Status"] = "Active"
                st.update_user(user_id,user_Data)
                print("Your Account Is Unlocked Now")
            else : print("Incorrect Pin.")

        elif SeQu != None:
            sq = tuple(user_Data["Security Question"].items())[0][0]
            sqa = tuple(user_Data["Security Question"].items())[0][1]
            ans = input(f"{sq} : ")
            if ans.lower() == sqa.lower():
                user_Data["Activity"] = "UNLOCKED"
                st.update_user(user_id,user_Data)
                print("Your Account Is Unlocked Now")
    else:
        print("Your Account is Already Unlocked.")
        return None
