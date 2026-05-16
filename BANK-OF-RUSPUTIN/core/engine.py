import core.storage as st
import core.auth as at
import core.validators as vl




def deposit(user_id,user_data:dict, amount:float = 0.0):
    if user_data["Status"] == "Active":
        user_balance = user_data["balance"]

        history = vl.tran_a(amount,"d")
        user_data["balance"] = str(float(user_balance) + amount)
        user_data["transaction_history"].append(history)
        if vl.transaction_balance_checker(user_data):
            st.update_user(user_id,user_data)
            print("The Amount has Successfull Creadited To Your Account.")
        else:
            user_data["balance"] = user_balance
            user_data["transaction_history"].pop()
            print("Your Transaction is Unfair! Changes rolled back.")
    else:print("Sorry! Cannot Deposit/Withdraw Money : Your Account is Locked.")


def withdraw(user_id,user_data:dict, amount:float = 0):
    if user_data["Status"] == "Active":
        user_balance = user_data["balance"]

        history = vl.tran_a(amount,"w")
        # print(history)
        # print(user_data["balance"])
        
        if float(user_balance) >= amount:
            user_data["balance"] = str(float(user_balance) - amount)
        else:
            print("Cannot withdraw! Invalid Amount.")
            return ""
        # print(user_data["balance"])
        user_data["transaction_history"].append(history)
        if vl.transaction_balance_checker(user_data):
            st.update_user(user_id,user_data)
            print("The Amount has Successfull Debited From Your Account.")
        else:# Rollback logic
            user_data["balance"] = user_balance
            user_data["transaction_history"].pop()
            print("Your Transaction is Unfair! Changes rolled back.")
    else:print("Sorry! Cannot Deposit/Withdraw Money : Your Account is Locked.")


def transaction_history(user_id,is_logined = False,user_data = None):
    if not is_logined:
        user_data = at.Login_check(user_id)
    
    if user_data != None and vl.transaction_balance_checker(user_data):
        print("Your Transactions :")
    
        tranB,tranT = vl.transaction_convertor(user_data)
    
        for i,tran in enumerate(tranB,start=0):
            print(f"Your Account was Credited with: {vl.un_balance(tran)} on {tranT[i]}" if tran > 0 else f"Your Account was Debited with: {vl.un_balance(tran)} on {tranT[i]}")


def change_pin(user_id = None,current_pin = None):
    if user_id == None:current_pin = input("Enter Your User ID : ")
    if current_pin == None:current_pin = input("Enter Your Current Pin : ")
    user_data, is_logined = at.Login_check(user_id,current_pin)
    while is_logined:
        new_pin = input("Enter New pin : ")
        if new_pin == current_pin:print("Can not user Previous pin As New Pin.")
        elif len(new_pin) != 4:print("The Length of The Pin Should be 4 digit.")
        elif not new_pin.isalnum(): print("Cannot use Charcter as Pin")
        else:
            user_data["PIN"] = new_pin
            print(user_data["PIN"])
            print("Your Pin Has Successfully Changed.")
            st.update_user(user_id,user_data)
            return None
        
