import time

print("Please insert Your CARD")

time.sleep(5)

password = 1234

pin = int(input("enter your atm pin"))

if pin == password:
    balance = 5000

    while True:
        print(""" 
        1 = balance
        2 = withdraw balance
        3 = deposit balance
        4 = exit
        """)

        try:
            option = int(input("please enter your choice"))
        except:
            print("please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("please enter withdraw_amount"))
            balance -= withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your updated balance is {balance}")

        elif option == 3:
            deposit_amount = int(input("please enter deposit_amount"))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")

        elif option == 4:
            break

        else:
            print("please select a valid option")
else:
    print("wrong pin please try again")
