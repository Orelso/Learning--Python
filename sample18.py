password = input("Password:")
rpassword = input("Repeat password:")

while password != rpassword:
    print("They do not match!")
    rpassword = input("Repeat password:")

print("User account created!")
