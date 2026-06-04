# Count Words and Characters (Without Blank Spaces)

s = input("Enter a string: ")

char_count = 0
word_count = 1

for ch in s:
    
    if ch != ' ':
        char_count = char_count + 1
    
    if ch == ' ':
        word_count = word_count + 1

print("Number of characters:", char_count)
print("Number of words:", word_count)