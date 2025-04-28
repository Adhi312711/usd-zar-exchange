# Define the exchange rate
exchange_rate = 20  # 1 USD to 20 ZAR

# Define functions to calculate the buying and selling prices
def calculate_purchase_price(amount, is_usd):
    if is_usd:
        return amount / exchange_rate
    else:
        return amount * exchange_rate * 0.925

def calculate_sale_price(amount, is_usd):
    if is_usd:
        if amount <= 5000:
            return amount * 1.05
        elif amount <= 10000:
            return amount * 1.025
        else:
            return amount * 1.01
    else:
        return amount / exchange_rate

# Define a function to handle the exchange
def exchange_currency():
    print("Select option:")
    print("1. Buy USD")
    print("2. Sell USD")
    print("3. Buy ZAR")
    print("4. Sell ZAR")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        amount = float(input("Enter amount: "))
        total_purchase_price = calculate_purchase_price(amount, True)
        profit = amount - total_purchase_price
        print(f"Total USD Bought: ${amount:.2f}")
        print(f"In ZAR: R{total_purchase_price:.2f}")
        print(f"Total Purchase Price: R{total_purchase_price:.2f}")
        print(f"Total Profit: R{profit:.2f}")
    elif choice == "2":
        amount = float(input("Enter amount: "))
        total_sale_price = calculate_sale_price(amount, True)
        profit = total_sale_price - amount
        print(f"Total USD Sold: ${amount:.2f}")
        print(f"In ZAR: R{total_sale_price:.2f}")
        print(f"Selling price: R{total_sale_price:.2f}")
        print(f"Total profit: R{profit:.2f}")
    elif choice == "3":
        amount = float(input("Enter amount: "))
        total_purchase_price = calculate_purchase_price(amount, False)
        profit = amount - total_purchase_price
        print(f"Total ZAR Bought: R{amount:.2f}")
        print(f"Total Purchase Price: ${total_purchase_price:.2f}")
        print(f"Total Profit: ${profit:.2f}")
        print(f"In ZAR: R{profit * exchange_rate:.2f}")
    elif choice == "4":
        amount = float(input("Enter amount: "))
        total_sale_price = calculate_sale_price(amount, False)
        profit = total_sale_price - amount
        print(f"Total ZAR Sold: R{amount:.2f}")
        print(f"In USD: ${total_sale_price:.2f}")
        print(f"Total profit: ${profit:.2f}")
        print(f"In ZAR: R{profit * exchange_rate:.2f}")
    else:
        print("Select a correct choice!")

