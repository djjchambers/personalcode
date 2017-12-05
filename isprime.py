from sys import argv

number = int(argv[1])

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            print('Not Prime')
    print('Prime!')
    
isprime(number)