#  try block
try:
    x = 10 / 2
    print("Result:", x)
except:
    print("Something went wrong")

# except block
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# else block
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division failed.")
else:
    print("Division successful:", x)

# finally block
try:
    x = 10 / 2
finally:
    print("This block always runs")

# Putting it all together
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero not allowed.")
else:
    print("Result:", result)
finally:
    print("Try-Except block finished.")

# Throwing in Python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    print(divide(10, 2))
except ValueError as e:
    print("Error:", e)

# Handling the exception with try-except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Exception caught:", e)

# Throwing custom exceptions
class NegativeValueError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeValueError("Age cannot be negative")

try:
    check_age(-5)
except NegativeValueError as e:
    print("Custom Exception:", e)

# No return function
def say_hello(name):
    if not name:
        return
    print("Hello", name)

say_hello("Tooba")
say_hello("")

# Returning None instead of no return
def find_even(num):
    if num % 2 != 0:
        return None
    return num

print("Even:", find_even(4))
print("Even:", find_even(5))

# Omitting return type hint
def greet(name):  # No type hint
    return f"Hello, {name}!"

print(greet("Ali"))