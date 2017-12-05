number = int(input("Type in a number> "))

if number % 2 == 0 and number % 4 == 0:
    print(f"{number} is even AND divisible by 4.")
elif number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")