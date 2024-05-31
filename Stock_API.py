import requests

class StockPortfolio:
    def __init__(self):
        self.stocks = {}
        self.api_key = 'RLIC6VG1W60VB2IH'

    def add_stock(self, ticker, shares):
        if ticker in self.stocks:
            self.stocks[ticker] += shares
        else:
            self.stocks[ticker] = shares

    def remove_stock(self, ticker, shares):
        if ticker in self.stocks:
            if shares >= self.stocks[ticker]:
                del self.stocks[ticker]
            else:
                self.stocks[ticker] -= shares

    def get_portfolio(self):
        return self.stocks

    def fetch_real_time_price(self, ticker):
        url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data['c']

    def get_portfolio_value(self):
        total_value = 0
        for ticker, shares in self.stocks.items():
            current_price = self.fetch_real_time_price(ticker)
            total_value += shares * current_price
        return total_value

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nPortfolio Tracker Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. View Portfolio Value")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(ticker, shares)
            print(f"Added {shares} shares of {ticker} to your portfolio.")

        elif choice == '2':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(ticker, shares)
            print(f"Removed {shares} shares of {ticker} from your portfolio.")

        elif choice == '3':
            print("Current Portfolio:")
            for ticker, shares in portfolio.get_portfolio().items():
                print(f"{ticker}: {shares} shares")

        elif choice == '4':
            total_value = portfolio.get_portfolio_value()
            print(f"Total Portfolio Value: ${total_value:.2f}")

        elif choice == '5':
            print("Exiting the portfolio tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
