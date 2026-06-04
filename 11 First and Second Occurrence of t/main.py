# Find First and Second Occurrence of 't'

s = input("Enter a string: ")

count = 0

for i in range(len(s)):
    
    if s[i] == 't':
        count = count + 1
        
        if count == 1:
            print("First occurrence of t at position:", i)
        
        elif count == 2:
            print("Second occurrence of t at position:", i)
            break