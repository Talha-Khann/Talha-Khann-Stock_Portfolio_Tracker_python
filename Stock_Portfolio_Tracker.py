
STOCK_PRICES = {
    "AAgPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

def display_available_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock} : ${price}")
    print("-" * 30)

def get_user_portfolio():
    portfolio = {}

    print("\nEnter stock details (type 'done' to finish):")

    while True:
        stock_name = input("Stock symbol: ").upper().strip()

        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print("Stock not available. Try again.")
            continue

        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Enter valid number.")
            continue

        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    detailed_summary = []

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * quantity
        total += investment

        detailed_summary.append(
            f"{stock} | Price: ${price} | Qty: {quantity} | Investment: ${investment}"
        )

    return total, detailed_summary

def save_to_file(summary, total):
    choice = input("\nSave result to file? (yes/no): ").lower().strip()

    if choice != "yes":
        return

    file_type = input("Save as (.txt/.csv): ").lower().strip()

    if file_type == ".txt":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("=" * 40 + "\n")
            for line in summary:
                file.write(line + "\n")
            file.write("=" * 40 + "\n")
            file.write(f"Total Investment: ${total}\n")

        print("Saved as portfolio_summary.txt")

    elif file_type == ".csv":
        with open("portfolio_summary.csv", "w") as file:
            file.write("Stock,Price,Quantity,Investment\n")
            for line in summary:
                parts = line.split(" | ")
                stock = parts[0]
                price = parts[1].split("$")[1]
                qty = parts[2].split(": ")[1]
                investment = parts[3].split("$")[1]
                file.write(f"{stock},{price},{qty},{investment}\n")

            file.write(f"\nTotal Investment,,,{total}\n")

        print("Saved as portfolio_summary.csv")

    else:
        print("Invalid file type. Not saved.")


def main():
    print("=" * 50)
    print("📊 STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    display_available_stocks()
    portfolio = get_user_portfolio()

    if not portfolio:
        print("\nNo stocks entered.")
        return

    total, summary = calculate_total_investment(portfolio)

    print("\nPortfolio Summary")
    print("=" * 40)
    for line in summary:
        print(line)

    print("=" * 40)
    print(f"Total Investment Value: ${total}")

    save_to_file(summary, total)

if __name__ == "__main__":
    main()
