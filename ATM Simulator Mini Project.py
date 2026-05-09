def clear(n):
    return int(n) if n == int(n) else n


print("        Welcome to the ATM Simulator")

balance = 10000

while True:

    print("\n===================================\n")
    print("\t   Menu")
    print("\t1.Balance")
    print("\t2.Deposit")
    print("\t3.Withdraw")
    print("\t4.Exit")

    try:
        inp = int(input("\nPlease sir, Give a command : "))

    except ValueError:
        print("\nPlease sir try again with an integer number")
        continue

    if inp == 1:
        print("\nYour Balance is :", balance)

    elif inp == 2:
       
        try:
            amount = float(input("\nPlease give your deposit amount : "))
        except ValueError:
            print("\nInvalid Amount")
            continue
        
        if amount<=0:
            print("\nNegative & zero amount is not allowed sir")
            continue    
        
        balance += amount
        balance = clear(balance)

        print("\nYour current total balance is :", balance)

    elif inp == 3:
      
        try:
            amnt = float(input("\nPlease give the amount you wanna withdraw : "))
        except ValueError:
            print("\nInvalid Amount")   
            continue
        
        if amnt<=0:
            print("\nNegative & zero amount is not allowed sir")
            continue    
        
        if (balance - amnt) < 200:
            print("\nYou need minimum 200tk in your account")
            continue

        balance -= amnt
        balance = clear(balance)

        print("\nYour current total balance is :", balance)

    elif inp == 4:
        print("\n===========Thank you Sir===========")
        break

    else:
        print("\nInvalid Command, Try again sir")
