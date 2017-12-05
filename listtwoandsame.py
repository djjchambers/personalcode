stufflist = ['123', '232', '3a3', '4zz4', '5123ab', '6']
count = 0

for chunk in stufflist:
    if len(chunk) > 2 and chunk[:1] == chunk[-1:]:
        count += 1
        
print(count)