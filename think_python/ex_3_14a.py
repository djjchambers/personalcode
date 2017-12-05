def right_justify(s):
    
    padding = 70-(len(s))
    print((padding * ' ') + s)
    
s = input("Input a string> ")
if len(s) < 71:
    right_justify(s)
elif len(s) > 70:
    print("String too long, must be less than 70 chars.")