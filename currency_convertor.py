rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "INR": 83.2,
    "GBP": 0.79,
    "JPY": 146.5
}

print("Available currencies:", ", ".join(rates.keys()))
from_currency = input("Convert from (currency code): ").upper()
to_currency = input("Convert to (currency code): ").upper()
amount = float(input(f"Amount in {from_currency}: "))

if from_currency in rates and to_currency in rates:
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Invalid currency code.")