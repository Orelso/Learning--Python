week = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
spend = float(input("How much money do you spend on groceries in a week?"))

daily = week  * price
weekly = daily + spend
total = weekly / 7
print("Average food expenditure")
print(f"Daily: {total} euros")
print(f"Weekly: {weekly} euros")
