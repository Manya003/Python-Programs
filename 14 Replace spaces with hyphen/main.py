# Replace Spaces with Hyphen '-'

s = "I love my country"

result = ""

for ch in s:
    
    if ch == ' ':
        result = result + '-'
    
    else:
        result = result + ch

print(result)