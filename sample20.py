attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1

    if code == "4321":
        success = True
        break

    print("Wrong")

if attempts > 1:
    print(f"Correct! It took you {attempts} attempts")
else:
    print("Correct! It only took you one single attempt!")
