# Simple ATM Interface

balance = 1000  # initial balance
pin = "1234"    # default pin

print("===== Welcome to ATM =====")
user_pin = input("Enter your PIN: ")

if user_pin == pin:
    while True:
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"Your balance is: ₹{balance}")
        
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"₹{amount} deposited successfully!")
        
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        
        elif choice == "4":
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid option, try again.")
else:
    print("Incorrect PIN. Access denied.")
