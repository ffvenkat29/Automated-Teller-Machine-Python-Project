users = {'62433570421':['John',12000, 1234],
         '62433570422':['Bob', 5000, 2244],
         '62433570423':['Charles', 1000, 9900],
         '62433570424':['David', 1500, 5678],
         '62433570425':['Reena',7500,9966]}
        
acc_no = input('Enter account number: ')
if acc_no in users:
    max_attempts = 3
    attempt = 1
    while attempt <= max_attempts:
        pin = int(input('Please enter your pin: '))
        db_pin = users[acc_no][-1]
        active_session = True
        if pin == db_pin:
            print('Logged in')
            break
        else:
            print('Wrong pin')
            remaining_attempts = max_attempts - attempt
            if remaining_attempts == 0:
                active_session = False
                print('Account locked. Please visit later')
            else:
                print(f'You have {remaining_attempts} attempts left....')
        attempt += 1
    transactions = []
    while active_session:
        print('Please enter your choice:')
        print()
        print('1.DEPOSIT')
        print('2.WITHDRAW')
        print('3.BALANCE ENQUIRY')
        print('4.PIN CHANGE')
        print('5.MINI STATEMENT')
        print('6.EXIT')
        print()
        choice = int(input('Enter your choice no: '))
        if choice == 1:
            amount = int(input('Please enter the amount for deposit: '))
            if amount > 0:
               users[acc_no][1] += amount
               transaction = f"{amount} deposited"
               transactions.append(transaction)
               print("Amount deposited")
            else:
               print('Invalid amount')
            
        elif choice == 2:
            amount = int(input('Please enter the amount for withdraw: '))
            in_bal = users[acc_no][1]
            if amount <= in_bal:
                users[acc_no][1] -= amount
                transaction = f"{amount} withdrawn"
                transactions.append(transaction)
                print('Amount withdrawn')
            else:
                print('Insufficient Funds')

        elif choice == 3:
            balance = users[acc_no][1]
            print(f'Current balance: {balance}')

        elif choice == 4:
            c_pin = int(input('Please enter your current pin: '))
            if c_pin == users[acc_no][-1]:
                new_pin = int(input('Please enter your new pin: '))
                confirm_pin = int(input('Please confirm new pin:'))
                if new_pin == confirm_pin:
                    users[acc_no][-1] = new_pin
                    print('Pin changed successfully')
                else:
                    print('Pin confirmation failed')
            else:
                print('Inccorect Pin')
        elif choice == 5:
            if len(transactions) <= 3: 
                min_statement = transactions[::-1]
            else:
                l = len(transactions)
                min_statement = transactions[:l-4:-1]

            print("-----------------------")
            print("     MINI STATEMENT    ")
            print("-----------------------")
            for i in min_statement:
                print(i)
                print()
        elif choice == 6:
            print('*******THANK YOU*******')
            break
        else:
            print('Invalid Choice')
else:
    print('Invalid User')