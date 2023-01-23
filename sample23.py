print("Please type in integer numbers. Type in 0 to finish.")
numbers = []
num = int(input("Number: "))
while num != 0:
    numbers.append(num)
    num = int(input("Number: "))
count = len(numbers)
sum_of_numbers = sum(numbers)
mean = sum_of_numbers/count
positive_numbers = len([x for x in numbers if x > 0])
negative_numbers = len([x for x in numbers if x < 0])
print("Numbers typed in", count)
print("The sum of the numbers is", sum_of_numbers)
print("The mean of the numbers is", mean)
print("Positive numbers", positive_numbers)
print("Negative numbers", negative_numbers)