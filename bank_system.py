accounts = {}

while True:
    print("\nWelcome to the Bank System")

    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if username in accounts:
            print("\nUsername already exists. Please try again")
        else:
            accounts[username] = {'password': password, 'balance': 0}
            print("\nAccount created successfully")

    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in accounts and accounts[username]['password'] == password:
            print("\nLogin successful")

            while True:
                print("\n1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                option = input("Enter your choice: ")

                if option == '1':
                    print("Balance:", accounts[username]["balance"])

                elif option == '2':
                    amount = float(input("Enter amount to deposit: "))
                    accounts[username]["balance"] += amount
                    print("\nDeposit successful. New balance:", accounts[username]["balance"])

                elif option == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    if amount <= accounts[username]["balance"]:
                        accounts[username]["balance"] -= amount
                        print("\nWithdrawal successful. New balance:", accounts[username]["balance"])
                    else:
                        print("\nNot enough balance. Please try again")

                elif option == '4':
                    print("\nLogging out...")
                    break

                else:
                    print("\nInvalid option. Please try again")

        else:
            print("\nWrong username or password")

    elif choice == '3':
        print("\nSee you next time")
        break

    else:
        print("\nInvalid choice. Please try again.")