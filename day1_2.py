import numpy as np

inp = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

ints = [str(i) for i in list(range(10))]
strints3 = ['one', 'two', 'six']
strints4 = ['four', 'five', 'nine']
strints5 = ['three', 'seven', 'eight']
strintsall = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

res = 0
for line in inp.split('\n'):
    arr = np.array(list(line))
    
    for i, char in enumerate(arr):
        if i < len(arr) - 2:
            strint3 = char+arr[i+1]+arr[i+2]
            #print(strint3)
            if strint3 in strints3:
                lefty = str(strintsall.index(strint3)+1)
                break
        
        if i < len(arr) - 3:
            strint4 = char+arr[i+1]+arr[i+2]+arr[i+3]
            #print(strint4)
            if strint4 in strints4:
                lefty = str(strintsall.index(strint4)+1)
                break
            
        if i < len(arr) - 4:
            strint5 = char+arr[i+1]+arr[i+2]+arr[i+3]+arr[i+4]
            #print(strint5)
            if strint5 in strints5:
                lefty = str(strintsall.index(strint5)+1)
                break
            
        if char in ints:
            lefty = char
            break
            
    for i, char in enumerate(arr[::-1]):
        tot = len(arr)
        
        if i < len(arr) - 1:
            strint3 = arr[tot-i-3]+arr[tot-i-2]+char
            #print(strint3)
            if strint3 in strints3:
                righty = str(strintsall.index(strint3)+1)
                break
        
        if i < len(arr) - 2:
            strint4 = arr[tot-i-4]+arr[tot-i-3]+arr[tot-i-2]+char
            #print(strint4)
            if strint4 in strints4:
                righty = str(strintsall.index(strint4)+1)
                break
        
        if i < len(arr) - 3:
            strint5 = arr[tot-i-5]+arr[tot-i-4]+arr[tot-i-3]+arr[tot-i-2]+char
            if strint5 in strints5:
                righty = str(strintsall.index(strint5)+1)
                break
            
        if char in ints:
            righty = char
            break
    
    print(lefty+righty)
    res += int(lefty + righty)

print(res)