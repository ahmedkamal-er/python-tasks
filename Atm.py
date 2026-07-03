def main():
    correcrt_pin = 1234
    balance=1000
    pin=int(input("Enter your pin: "))
     
    if pin!=correcrt_pin:
        print("Access denied. Incorrect pin.")
        return #it will end the program and start over using the pin again!
    
    while True: #loop will run until the user chooses to exit
        print("1- withdraw")
        print("2- check balance")
        print("3- exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Your balance is: ",balance)
            withdraw=int(input("Enter the amount to withdraw: "))
            if withdraw > balance:
                print("sorry, you have insufficient funds.")
            elif withdraw <= balance:
                balance-=withdraw
                print(f"you have withdrawn {withdraw}")
                print(f"your new balance is {balance}")
                print(f"operation successful. Thank you for banking with us.")
                continue 
            
        elif choice==2:
            print(f"your current balance is {balance}")
            another_transaction =input("do you want to do another transaction?: ").lower().strip()
            if another_transaction == "yes":
                continue #skip the rest of the loop and start from the beginning 
            elif another_transaction == "no":
                print("Thank you for banking with us.")
                return
            
        elif choice == 3:
            print("Thank you for banking with us.")
            return
            
        
        else:
            print("Invalid choice. Please try again.")
            continue 

if __name__ == "__main__":
    main()
