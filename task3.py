class CurrencyConverter:
    def _init_(self):
        # Define exchange rates manually
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 114.50,
            # Add more currencies and exchange rates as needed
        }

    def convert_currency(self, amount, from_currency, to_currency):
        # Convert currency based on the manually defined exchange rates
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates:
            rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
            converted_amount = amount * rate
            return converted_amount
        else:
            print("Invalid currency codes.")
            return None

if _name_ == "_main_":
    converter = CurrencyConverter()

    print("Available currencies:")
    print(", ".join(converter.exchange_rates.keys()))

    while True:
        # Input amount and currencies for conversion
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency code: ").upper()
        to_currency = input("Enter the target currency code: ").upper()

        # Perform the conversion
        converted_amount = converter.convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            print("Exiting.")
            break