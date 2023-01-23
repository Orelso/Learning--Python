codes = ""
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    codes += code + ", "
    if attempts == 10:
        print(f"{codes}")
        break
