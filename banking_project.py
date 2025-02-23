
import time
balance=100000

def money_transfer(name,password,balance):
    account_input=input(f"\nHello {name} Please Enter The Account Number Of Money Receiver :")
    if account_input.isdigit() and len(account_input)==10:
        print(F"\n{account_input} The Account Number Of Receiver You Entered :")
        confirmation=input("Enter Ok For Confirm The Account NO : ").lower()
        if confirmation=="ok":
            print(f"Your Current Account Balance Is ₹{balance} : ")
            amount_transfer=int(input("Enter The Amount You Want To Transfer : ₹"))
            if amount_transfer<=balance:
                transfer_password=input("Enter The Password To Transfer : ")
                if transfer_password==password:
                    balance=balance-amount_transfer  #creating new variable for balance to access in different form without any error. 
                    print("\nPlease Wait, We Processing Your Transaction : ")
                    for i in range (8, -1, -1):
                        print(f"Waiting Time {i}  Seconds ",end="\r")
                        time.sleep(1)    #timer added for more real looking
                    print("Your Money Transfer Is Completed :")
                    print(f"And Your Current Balance Is ₹{balance}.")
                    print("\nYou Are Redirect To Main Menu \nPlease Wait :")
                    for j in range(17, -1, -1):
                        print(f"Redirecting {j}  Seconds",end="\r")
                        time.sleep(1)
                    function(name,password,balance)
                else:
                    print("You Entered Wrong Password. ")
                    print("\nPlease Try Again : ") 
                    money_transfer(name,password,balance) 
            else:
                print("\nYou Entered Amount Is More Than Your Current Balance :")
                money_transfer(name,password,balance) 
        else:
            print("\nYou Entered Incorrect  Input For Conformation , So Try Again : ")
            money_transfer(name,password,balance) 
    else:
        print("You Entered Account Number Is Invaild Please Enter vaild Ten digits Account No , And Try Again")
        money_transfer(name,password,balance) 
        

def money_request(name,password,balance):
    account_request=input("\nEnter Account NO Of Money Sender : ")
    if account_request.isdigit() and len(account_request)==10:
        print(f"\n{account_request} The Account Number Of Sender You Entered : ")
        account_confirmation=input("Enter OK For Confirm The Account NO : ").lower()
        if account_confirmation=="ok":
            amount_request=int(input("Enter The Amount You Requesting : ₹"))
            if amount_request<10001:
                print("\nPlease Wait :")
                print("\n")
                for h in range(5, -1, -1):
                    print(f"We Processing Your Request {h}  Seconds",end="\r")
                    time.sleep(1)
                print("\nYour Request Sended To The Account Holder. Thank  You!")  
                print("\nYou Are Redirect To Main Menu \nPlease Wait :")
                for j in range(17, -1, -1):
                    print(f"Redirecting {j}  Seconds",end="\r")
                    time.sleep(1)
                function(name,password,balance)
            elif amount_request>10000:
                print("\nPlease Wait :")
                print("\n")
                for g in range(5, -1, -1):
                    print(f"We Processing Your Request {g}  Seconds",end="\r")
                    time.sleep(1)
                print("\nAmount Greater Than ₹10000 Can't Be Requested. Thank You! ")
                print("\n")
                print("You Are Redirect To Main Menu \nPlease Wait :")
                for i in range(17, -1, -1):
                    print(f"Redirecting {i}  Seconds",end="\r")
                    time.sleep(1)
                function(name,password,balance)
            else:
                print("Somthing Went Wrong. Please Try Again! ")
                money_request(name,password,balance)
        else:
            print("\nYou Entered Incorrect Input For Confimation, So Try Again : ")
            money_request(name,password,balance)
    else:
        print("You Entered Account Number Is Invaild Please Enter vaild Ten digits Account No , And Try Again")
        money_request(name,password,balance)

def money_deposit(name,password,balance):
    print("Here We Only Accept Multiple of 100's Only:")
    deposit_request=int(input("Enter The Amount Here : ₹"))
    print(f"We Checking Your Input Please Wait : ")
    print("\n")
    for i in range(10, -1, -1):
        print(f"Waiting Time {i}  Seconds ", end="\r" )
        time.sleep(1)   #timer added for more real looking 
    if deposit_request%100==0:
        print("\nVerification complete!")
        balance=balance+deposit_request   
        print(f"Your Deposit Amount Add To Your Current Balance")
        print(f"\nNew Balance ₹{balance}")
        print("\nYou Are Redirect To Main Menu \nPlease Wait :")
        print("\n")
        for j in range(17, -1, -1):
            print(f"Redirecting {j}  Seconds",end="\r")
            time.sleep(1)
        function(name,password,balance)
    else:
        print("\n")
        print(f"Sorry ₹{deposit_request} Is Not Multiple of 100 : ")
        print("Please Try Again. ")
        print("\n")
        money_deposit(name,password,balance)

def money_Withdrawal(name,password,balance):
    print("\nHere You Can Withdraw multiple Of 100 only : ")
    withdrawal_request=int(input("Enter Amount Here : ₹"))
    if withdrawal_request%100==0:
        password_check=input("Enter Your Password To Confirm : ")
        if password_check==password:
            print("We Are Processing Your Transaction. ")
            print("\n")
            for i in range (6, -1, -1):
                print(f"Please Wait {i}  Seconds.",end="\r")
                time.sleep(1)
            balance=balance-withdrawal_request
            print("\nYou Transaction Completed. ")
            print(f"Curent Balance ₹{balance}")
            print("\n")
            print("\nYou Are Redirect To Main Menu \nPlease Wait :")
            print("\n")
            for j in range(17, -1, -1):
                print(f"Redirecting {j}  Seconds",end="\r")
                time.sleep(1)
            function(name,password,balance)
        else:
            print("\nYou Entered Wrong Password, So Please Try Again : ")
            for a in range (6, -1, -1):
                print(f"Please Wait {a}  Seconds.",end="\r")
                time.sleep(1)
            print("\n")
            return money_Withdrawal(name,password,balance)
    else:
        print(f"Sorry ₹{withdrawal_request} Is Not Multiple of 100 : ")
        money_Withdrawal(name,password,balance)

def view_balance(name,password,balance):
    print(f"Your Current Balance ₹{balance}. ")
    time.sleep(5)
    print("\n")
    return_view=input("Enter OK To Go Main Menu : ").lower()
    if return_view=="ok":
        for j in range(10, -1, -1):
            print(f"Redirecting {j}  Seconds",end="\r")
            time.sleep(1)
        function(name,password,balance)
    else:
        print("\nThank You. For Using KDFC Bank ATM Services. ")

def function(name,password,balance):
    print("""\n
    1.Money Transfer 
    2.Money Request 
    3.Money Deposit
    4.Money Withdrawal
    5.View Balance 
    6.Exit
    """)
    function_input=int(input("\nEnter The Number Of The Function Like (1 to 6) : "))
    print(function_input)

    if function_input==1:
        money_transfer(name,password,balance)
    elif function_input==2:
        money_request(name,password,balance)
    elif function_input==3:
        money_deposit(name,password,balance)
    elif function_input==4:
        money_Withdrawal(name,password,balance)
    elif function_input==5:
        view_balance(name,password,balance)
    elif function_input==6:
        print("\nThanks For Visting KDFC Bank ATM Servier. ")
    else:
        print("\n You Enter The Wrong Input So Please Try One More Time")
        return function()

def login (balance):
    print("\nWelcome To My ATM Banking Project.")
    print("""
            Hello Your Id And Password Are What You Entering in name +1 like name=kk id is KK1\n
            Password like name +2 Example kk2 For password.
    """)
    name=input("\nEnter Your Name : ")  #input for name to print the welcome message to custmer after login is completed
    id_input=input("Enter Your ID Here : ")
    password_input=input("Enter Your Password Here : ")
    id=(f"{name}1")
    password=(f"{name}2")
    if id_input==id:
        if password_input==password:
            print(f"\nWelcome {name} To KDFC Bank ATM Service .")
            function(name,password,balance)
        else:
            print("\nYou Given Wrong ID and Password So you Can't Login to Your ID :")

    else:
        print("\nYou Given Wrong ID and Password So you Can't Login to Your ID :")


login(balance)
