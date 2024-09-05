import time
import sys

user_balance = 100

trans1 = "NA"
trans2 = "NA"
trans3 = "NA"
trans4 = "NA"
trans5 = "NA"
trans6 = "NA"
trans7 = "NA"
trans8 = "NA"
trans9 = "NA"
trans10 = "NA"

time.sleep(0.75)
print('''P.S The code is 1212.
Don't use caps.
You can only see your previous 10 transactions.''')
time.sleep(1)
print("Welcome to jayWay Banking.")
print()
time.sleep(1)
attempts = True
while attempts == True:
    attempt1 = input("Please enter PIN: ")
    if attempt1 == "1212":
        print("Correct PIN")
        time.sleep(1)
        break
    else:
        print("Incorrect")
        time.sleep(0.75)
        attempt2 = input("Please enter correct PIN: ")
        if attempt2 == "1212":
            print("Correct PIN ")
            break
        else:
            print("Incorrect PIN")
            time.sleep(0.75)
            print("You have 1 more attempt")
            attempt3 = input("Please enter correct PIN: ")
            if attempt3 == "1212":
                print("Correct PIN:")
                break

            else:
                print("Incorrect PIN")
                print("Wait 2 minutes to try again (or restart machine)")
                time.sleep(120)
                print()

yes = 0
valid_option = True
while valid_option == True:
    time.sleep(0.75)
    menu = input('''
Please select an option:
                 
Welcome to jayWay Banking
1 - Display Balance
2 - Withdraw Funds
3 - Deposit Funds
4 - Print list of transactions
9 - Return Card
                 
---> : ''')
    print()
    if menu == "1":
        print("Display Balance")
        print("$", user_balance)
        print()
        time.sleep(0.25)

    elif menu == "2":
        print("Withdraw Funds")
        time.sleep(0.75)
        wf = int(input('''
How much would you like to withdraw?
Your options are:
10:
20:
50:
100:
7 - Other(must be a multiple of 10)
8 - Return to main menu
9 - Return card

--->: '''))
        
        if wf == user_balance:
            print("You broke, you now have $0 in your bank account")
            user_balance = 0
            never = "Withdrew", wf

        elif wf > user_balance:
            print("Your money is not enough")
            never = 0
            yes = yes - 1

        elif wf == 10:
            print("You have successfully withdrawn $ 10, you now have", user_balance - 10)
            user_balance = user_balance - wf
            never = "Withdrew", wf

        elif wf == 20:
            print("You have successfully withdrawn $ 20, you now have", user_balance - 20)
            user_balance = user_balance - wf
            never = "Withdrew", wf
        
        elif wf == 50:
            print("You have successfully withdrawn $ 50, you now have", user_balance - 50)
            user_balance = user_balance - wf
            never = "Withdrew", wf

        elif wf == 100:
            print("You have successfully withdrawn $ 100, you now have", user_balance - 100)
            user_balance = user_balance - wf
            never = "Withdrew", wf

        elif wf == 7:
            print("Other amount")
            ea = int(input("How much would you like to withdraw?: "))
            if ea == user_balance:
                print("You broke, you now have $0 in your bank account")
                user_balance = 0
                never = "Withdrew", ea
            
            elif ea > user_balance:
                print("You do not have enough money")
                never = never
                yes = yes - 1

            elif ea % 10 == 0:
                print("You have successfully withdrawn $", ea, "you now have $", user_balance - ea)
                user_balance = user_balance - ea
                never = "Withdrew", ea

            else:
                print("Invalid")
                print("Make sure it is a multiple of 10 and numbers only")
                never = never
                yes = yes - 1

        elif wf == 8:
            print()
            never = never
            yes = yes - 1

        elif wf == 9:
            print("Thank you for banking at jayWay Bank ^.^")
            sys.exit()
        else:
            print("Invalid")
            yes = yes - 1

        yes = yes + 1
        if yes > 10:
            trans1 = trans2
            trans2 = trans3
            trans3 = trans4
            trans4 = trans5
            trans5 = trans6
            trans6 = trans7
            trans7 = trans8
            trans8 = trans9
            trans9 = trans10
            trans10 = never

        elif yes == 1:
            trans1 = never

        elif yes == 2:
            trans2 = never

        elif yes == 3:
            tran3 = never

        elif yes == 4:
            trans4 = never

        elif yes == 5:
            trans5 = never

        elif yes == 6:
            trans6 = never

        elif yes == 7:
            trans7 = never

        elif yes == 8:
            trans8 = never

        elif yes == 9:
            trans9 = never

        elif yes == 10:
            trans10 = never

    elif menu == "3":
        print("Deposit Funds")
        EA = int(input('''
Choose an option:
1 - Deposit
2 - Return to main menu
9 - Return Credit Card    
--->: '''))
        if EA == 1:
            dp = int(input("How much would you like to deposit?: "))
            if dp > 0:
                print("You have successfully deposited", dp, "you now have $", user_balance + dp)
                user_balance = user_balance + dp
                never = "Deposited", dp

            elif dp < 0:
                print("You can not use negative(-ve) numbers")
                never = never
                yes = yes - 1

            elif EA == 2:
                print()
                never = never
                yes = yes - 1

            elif EA == 9:
                print("Thank you for using jayWay Banking ^.^")
                sys.exit()

            yes = yes + 1
            if yes > 10:
                trans1 = trans2
                trans2 = trans3
                trans3 = trans4
                trans4 = trans5
                trans5 = trans6
                trans6 = trans7
                trans7 = trans8
                trans8 = trans9
                trans9 = trans10
                trans10 = never

            elif yes == 1:
                trans1 = never

            elif yes == 2:
                trans2 = never

            elif yes == 3:
                trans3 = never

            elif yes == 4:
                trans4 = never

            elif yes == 5:
                trans5 = never

            elif yes == 6:
                trans6 = never

            elif yes == 7:
                trans7 = never

            elif yes == 8:
                trans8 = never

            elif yes == 9:
                trans9 = never

            elif yes == 10:
                trans10 = never

        elif menu == "4":
            print("Print List Of Transactions")
            time.sleep(0.75)
            print()
            print(trans1)
            print(trans2)
            print(trans3)
            print(trans4)
            print(trans5)
            print(trans6)
            print(trans7)
            print(trans8)
            print(trans9)
            print(trans10)

        elif menu == "9":
            print("Thank you for choosing jayWay Banking ^.^")
            sys.exit

        else:
            print("Please Choose A Valid Option")