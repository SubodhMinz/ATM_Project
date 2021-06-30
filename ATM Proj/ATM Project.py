# This is a ATM Program
# The password is 1234
import time

balance = 200
print("Wel Come to Swiss Bank")
passAtempt = 0
while(True):
    password = int(input("Enter your Password : "))
    if password == 1234:
        while(True):
            print("1 for balance Inqurey\n2 for withdrole\n3 for diposit")
            option = int(input("Plese Choose anyone : "))
            if option == 1:
                print(f"Your have ${balance}")
                print("Would you like to continue y/n")
                ysno = input(": ")
                if ysno == "y":
                    continue
                else:
                    print("Thank you for banking with Swiss Bank")
                    exit()

            elif option == 2:
                withdrole = int(input("Enter the Amount : "))
                balance = balance-withdrole
                print("Plese wait, your request is being process")
                time.sleep(2)
                print("Plese take your widthrole money")
                print(f"Your new balance is ${balance}")
                print("Would you like to continue y/n")
                ysno = input(": ")
                if ysno == "y":
                    continue
                else:
                    print("Thank you for banking with Swiss Bank")
                    exit()

            elif option == 3:
                diposit = int(input("Enter the diposit Amout : "))
                balance = balance+diposit
                print(f"Your curent balance is ${balance}")
                print("Would you like to continue y/n")
                ysno = input(": ")
                if ysno == "y":
                    continue
                else:
                    print("Thank you for banking with Swiss Bank")
                    exit()

            else:
                print("Plese ente the Right One")

    else:
        passAtempt+=1
        print("Plesr enter the right Password")
        if passAtempt==2:
            print("Would you like to continue y/n")
            ysno = input(": ")
            if ysno == "y":
                continue
            else:
                print("Thank you for visiting Swiss Bank")
                exit()
