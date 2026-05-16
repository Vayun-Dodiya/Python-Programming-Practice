from datetime import datetime

def tran_a(amount,a="w"):
    now = datetime.now()
    if a.lower() == "d" and amount >= 0:return f"{now.strftime("%d-%m-%Y at %H:%M:%S")} | {amount}D"
    if a.lower() == "w" and amount >= 0:return f"{now.strftime("%d-%m-%Y at %H:%M:%S")} | {amount}W"
    # else:return f"{now.strftime("%d-%m-%Y at %H:%M:%S")} | {amount}"

def un_balance(balance:str)->str:
    return f"$ {float(balance):,}"

def transaction_balance_checker(user_data):
    transaction_history = transaction_convertor(user_data)[0]
    balance = float(user_data["balance"])
    C_balance = 0.0
    for trans in transaction_history:
        C_balance = C_balance + trans
    if balance == C_balance:
        return True
    else:
        return False
    
def transaction_convertor(user_data:dict) -> list:
    transaction_history_ = []
    transaction_history_time = []

    transaction_ = user_data["transaction_history"]
    # print(transaction_) #
    
    for tran in transaction_:
        tran_t,tran_b = tran.split("|")
        transaction_history_time.append(tran_t)
        # print(tran_t+"-"+tran_b) #
        if tran_b.endswith("D"):
            transaction_history_.append(float(tran_b[:-1])*1)
        if tran_b.endswith("W"):
            transaction_history_.append(float(tran_b[:-1])*-1)
    
    return [transaction_history_,transaction_history_time]