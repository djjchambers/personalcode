num = int(input("Type in a number: "))
check = int(input("Type in another number to divide it by: "))

if num // check == 0:
    print(f"{num} divides by {check} exactly {num / check} times.")
elif num // check != 0:
    print(f"{num} divides by {check} {num // check} times with {num % check} left over.")
else:
    print("What the f is going on?")