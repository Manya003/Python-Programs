# main.py

# Importing module
from calculator import Calculator

# Importing package
from mypackage.greetings import say_hello

# Creating object of class
calc = Calculator()

print("Addition:", calc.add(20, 5))
print("Subtraction:", calc.subtract(20, 5))

print(say_hello("Divya"))