num = int(input('enter number: '))

print([item for item in range(1, num) if num % item == 0])