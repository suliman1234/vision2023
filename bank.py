print("Welcome to our bank")

restart= "y"
pin1=1234
user="sam123"
chances=3
balance= 2000.25

while chances >0:
    username = str(input("Please enter your username"))
    pin= int(input("please Enter your pin"))
    if pin == pin1 and username== user:
        print('succussful, welcome to our bank where we will try to steal you as much as possible')
        while restart not in ('no', 'n'):
            print('please enter 1 for withdrawal\n'
                  'please enter 2 to deposit\n'
                  'please enter 3 to see balance\n'
                  'please enter 4 to return card ')
            option = int(input("Enter a number"))
            if option ==1:
                w= float(input('how much would you like to withdraw'))
                balance= balance-w
                if balance < 0:
                    print("Sorry you don't have enough money\n and also go look for a job")

                else:
                    if balance < 1000:
                        print('Now, you have only', balance, 'Feel bad for you\n')
                        restart = input('Would you like another service? y/n')
                    else:
                        print('you have', balance, 'left in your account\n')
                        restart=input('Would you like another service? y/n')

            if option == 2:
                d=float(input('How much would you like to deposit'))
                balance= balance + d
                print("Your current balance is", balance)
                restart = input('Would you like another service? y/n')

            if option == 3:

                print('your current balance is', balance)
                restart = input('Would you like another service?y/n')

            if option == 4:
                print('Thanks for being loyal, See you later')
                break


            if option not in (1,2,3,4):
                print('Wrong number, try to focus on the options this time')

    elif pin != 1234 or user != username:
        chances = chances - 1
        print("Your username or password is wrong \n", 'you have', chances, "more tries")
    else: print('Thanks for being loyal to our bank')

print('Go know your passworddd')

