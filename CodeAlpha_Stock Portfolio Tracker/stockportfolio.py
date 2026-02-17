stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 300
}

print("📈 Welcome to Stock Portfolio Tracker\n")

total_investment = 0
portfolio = {}

print("Available Stocks and Prices (in ₹):")
for stock, price in stock_prices.items():
    print(stock, ":", "₹", price)

print("\nEnter stock details (type 'done' to finish)\n")

while True:
    stock_name = input("Enter stock name: ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        
        investment_value = stock_prices[stock_name] * quantity
        total_investment += investment_value
        
        portfolio[stock_name] = quantity
        
        print("Added", stock_name, "Investment Value: ₹", investment_value, "\n")
    else:
        print("Stock not found in list. Please try again.\n")

print("\n📊 Portfolio Summary")
print("---------------------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(stock, "-", quantity, "shares", ":", "₹", value)

print("---------------------------")
print("Total Investment Value: ₹", total_investment)

save_option = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save_option == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("---------------------------\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock} - {quantity} shares : ₹ {value}\n")
        file.write("---------------------------\n")
        file.write(f"Total Investment Value: ₹ {total_investment}\n")
    
    print("✅ Portfolio saved to portfolio.txt")
else:
    print("File not saved.")
