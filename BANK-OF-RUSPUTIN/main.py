import core.auth as at
import core.engine as eg
import core.storage as st
import core.validators as vl
import time
def ftrs(is_logined = False):

    if not is_logined:
        print("Login To Your Accound to Use Below Features :")
    else:
        print("\nEnter Your Choice.")
    print("1. Login")
    print("2. Check Balance")
    print("3. See Transaction History")
    print("4. Withdraw")
    print("5. Deposit")
    print("6. Change PIN")
    print("7. UnLock Your Account")
    print("8. Log Out")
    try:
        return int(input("Enter The Number Of Your Choice :")) 
    except:
        return 
tramade = None
user_id , UserData , is_logined  =  None , None , False
print("Welcome the Bank of RASPUTIN".center(190))
# user_id = "1001"
# PIN = "4482"
# user_data,is_logined = at.Login_check(user_id,PIN)
# print(eg.change_pin(user_id,PIN))
while True:
    print("Enter Your User ID to Login")
    user_id = input("Enter Your User ID : ")
    UserData,is_logined = at.Login_check(user_id)

    if UserData != None and is_logined:
    
        while is_logined:
            time.sleep(1.5)
            order = ftrs(is_logined=is_logined)
            time.sleep(2)
            match order:
    
                case 1:
                    if is_logined:
                        print("You have Already Logined.")
                    else:
                        print("Enter Your User ID to Login")
                        user_id = input("Enter Your User ID : ")
                        UserData,is_logined = at.Login_check(user_id)
                        
                case 2:
                    if vl.transaction_balance_checker(UserData):
                        print(f"Your Current Account Balance : {vl.un_balance(UserData["balance"])}")
    
                case 3:
                    if vl.transaction_balance_checker(UserData):
                        eg.transaction_history(user_id,is_logined,UserData)
                    else:
                        print("Your Transaction are unfair.")
    
                case 4:
                    #widraw
                    try:
                        amount = float(input("Enter the Amount You want to Widraw : "))
                    except:
                        print("Invalid Input")
                        amount = float(input("Enter the Amount You want to Widraw : "))
                    eg.withdraw(user_id,UserData,amount)
    
                case 5:
                    #deposit
                    try:
                        amount = float(input("Enter the Amount You want to Deposit : "))
                    except:
                        print("Invalid Input")
                        amount = float(input("Enter the Amount You want to Deposit : "))
                    eg.deposit(user_id,UserData,amount)
                    
                case 6:
                    #change pin
                    eg.change_pin(user_id)
    
                case 7:
                    #unlock
                    # pin = input("Enter Your Current pin To UNLOCK Your Accont : ")


                    '''
                    this function is still under construcion so do not mind if you any function in the other mudule which are related to this funciton in any possible way.
                    thank you
                    '''
                    
                    user_id = input("Enter Your User ID : ")
                    sq = None
                    ex = int(input("Enter 1 if you want to Unlock Your Account via Admin Pin.\nEnter 2 if you want to Unlock Your Account via Security Question.\nEnter :"))
                    if ex == 1:ap = int(input("Enter Admin Pin (press 0 if don't have): "))
                    elif ex == 2: sq = 0;ap = None
                    at.unlock(user_id,ap,sq)

                case 8:
                    user_id, UserData = None, None;break
    
                case 9:raise
    else:break
    
