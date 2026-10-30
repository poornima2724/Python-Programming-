stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

total = 0

print("Welcome to Stock Portfolio Tracker")

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks and quantity > 0:
        investment = stocks[name] * quantity
        total += investment

        print("Stock:", name)
        print("Investment:", investment)
    else:
        print("Invalid stock name or quantity!")

print("\nTotal Investment Value:", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: " + str(total))

print("Portfolio saved successfully!")
