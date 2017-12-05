# define function that brings in two arguments when it's called, NB i and s are local variables to the function.
def print_nums_in_list(i, s):
    # assign two variables, a counter and the empty list
    loop_count = 0
    numbers = []


    # take i to be the upper limit of the loop
    while loop_count < i:
        print(f"At the top loop_count is {loop_count}")
        numbers.append(loop_count)
    
        # s is the step
        loop_count += s
        # print the list
        print("Numbers now: ", numbers)
        print(f"At the bottom is {loop_count}")
    
    # print the numbers in sequence from the list
    print("The numbers: ")

    # declare the new variable, step through the list using num as the index and printing out the contents each pass of the loop
    for num in numbers:
        print(num)
        
# Just for my own sanity I put this in, because I assume it's good practice to define your functions first?
print("Here's the beginning of the program.")

# declare two variables which get input from the user. These are equivalent to the two arguments passed to the function.
iterations = int(input("How many items? "))
step_to_increment = int(input("How big an increment? "))

#This is the bit that blows my mind. Calling the function using these two global variables, but the function maps them onto two local variables inside it. Pchowwwww!
print_nums_in_list(iterations, step_to_increment)