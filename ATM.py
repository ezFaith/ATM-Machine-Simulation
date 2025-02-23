from datetime import datetime

class ATMMachine:
    def __init__(self):
        # Initialize with default values
        self.balance = 1000.0  # Initial account balance
        self.pin = "1234"      # Default PIN
        self.transactions = [] # Stores transaction history

    def check_balance(self):
        """Return current account balance"""
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw specified amount if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            # Record transaction with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(
                f"{timestamp} - Withdrawal: ${amount:.2f}. Balance: ${self.balance:.2f}"
            )
            return True
        return False

    def deposit(self, amount):
        """Deposit specified amount into account"""
        if amount > 0:
            self.balance += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(
                f"{timestamp} - Deposit: ${amount:.2f}. Balance: ${self.balance:.2f}"
            )
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        """
        Change PIN if old PIN is correct and new PIN is valid.
        Returns True if successful, False otherwise.
        """
        if old_pin == self.pin and new_pin.isdigit() and len(new_pin) == 4:
            self.pin = new_pin
            return True
        return False

    def get_transaction_history(self):
        """Return copy of transaction history"""
        return self.transactions.copy()


def main():
    # Initialize ATM
    atm = ATMMachine()

    # Login Process
    attempts = 0
    max_attempts = 3
    print("Welcome to the ATM!")
    while attempts < max_attempts:
        pin_input = input("Enter your PIN: ")
        if pin_input == atm.pin:
            break
        attempts += 1
        print(f"Invalid PIN. Attempts remaining: {max_attempts - attempts}")
    else:
        print("Too many incorrect attempts. Account locked.")
        return

    # Main Menu
    while True:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Balance Inquiry
            print(f"\nCurrent Balance: ${atm.check_balance():.2f}")

        elif choice == "2":
            # Cash Withdrawal
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                if atm.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds or invalid amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "3":
            # Cash Deposit
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                if atm.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "4":
            # PIN Change
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN (4 digits): ")
            confirm_pin = input("Confirm new PIN: ")
            
            if new_pin != confirm_pin:
                print("PINs do not match.")
            elif not new_pin.isdigit() or len(new_pin) != 4:
                print("PIN must be 4 digits.")
            else:
                if atm.change_pin(old_pin, new_pin):
                    print("PIN changed successfully.")
                else:
                    print("Incorrect current PIN.")

        elif choice == "5":
            # Transaction History
            history = atm.get_transaction_history()
            if not history:
                print("\nNo transactions available.")
            else:
                print("\nTransaction History:")
                for transaction in history:
                    print(transaction)

        elif choice == "6":
            # Exit
            print("\nThank you for using the ATM. Goodbye!")
            break

        else:
            print("\nInvalid selection. Please try again.")


if __name__ == "__main__":
    main()