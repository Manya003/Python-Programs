# x = lambda a : a + 10
# print(x(5))

is_perfect_square = lambda n: n >= 0 and int(n**0.5) ** 2 == n

# Example
print(is_perfect_square(4))   # True
print(is_perfect_square(10))  # False
print(is_perfect_square(25))  # True