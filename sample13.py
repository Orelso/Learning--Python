wage = float(input("Hourly wage: "))
worked = float(int(input("Hours worked: ")))
day = (input("Day of the week: "))

if day == "Sunday":
    print(f"Daily wages: {(wage * worked) * 2} euros")
elif day == day:
    print(f"Daily wages: {wage * worked} euros")
