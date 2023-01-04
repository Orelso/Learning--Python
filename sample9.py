students = int(input("How many students on the course?"))
gSize = int(input("Desired group size?"))

total = (students // gSize ) 

if students % gSize > 0:
    print("Number of groups formed:",total + 1)
elif total:
    print("Number of groups formed:", total )

