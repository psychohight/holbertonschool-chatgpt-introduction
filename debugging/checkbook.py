class Checkbook:
    """A class to represent a checkbook for managing a balance via deposits and withdrawals."""

    def __init__(self):
        """Initialize a new checkbook instance with a balance of zero."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
        amount (float): The amount of money to deposit.

        Prints the deposit action and the new balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw.

        Prints the withdrawal action and the new balance, or a warning if insufficient funds.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to run the checkbook application.
    
    Allows the user to repeatedly deposit money, withdraw money, check the balance, or exit the program.
    """
    cb = Checkbook()  # Create a new Checkbook instance
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

