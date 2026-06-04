# Shuffle Odd and Even Words

s = input("Enter a sentence: ")

words = []
word = ""

# Store words manually
for ch in s:
    
    if ch != ' ':
        word = word + ch
    
    else:
        words = words + [word]
        word = ""

# Add last word
words = words + [word]

result = ""

# Swap words in pairs
for i in range(0, len(words), 2):
    
    if i + 1 < len(words):
        result = result + words[i + 1] + " " + words[i] + " "
    
    else:
        result = result + words[i]

print(result)