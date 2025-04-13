#  Built-in Function Example
print("Length of string:", len("Hello"))

# Function from a Built-in Module Example
print("Random number:", __import__('random').randint(1, 10))

# User-defined Function
def greet(name):
    print(f"Hello, {name}!")

greet("Areeba")

# Pass by Reference vs Value
def modify_list(mylist):
    mylist.append(99)

nums = [1, 2, 3]
modify_list(nums)
print("Modified list:", nums)

# Default Argument
def say_hi(name="Stranger"):
    print("Hi", name)

say_hi()
say_hi("Ali")

# Positional-only
def subtract(x, y, /):
    return x - y

# Keyword-only
def divide(*, a, b):
    return a / b

# Arbitrary positional arguments
def total_sum(*args):
    return sum(args)

# Arbitrary keyword arguments
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Subtract:", subtract(5, 2))
print("Divide:", divide(a=10, b=2))
print("Sum:", total_sum(1, 2, 3, 4))
describe_person(name="Sara", age=25)

#  Function with Return
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print("Multiplication Result:", result)

# Anonymous Function
square = lambda x: x * x
print("Square using lambda:", square(6))

#Variable Scope
x = "global"

def scope_demo():
    x = "local"
    print("Inside function:", x)

scope_demo()
print("Outside function:", x)

#  Arbitrary Keyword Arguments
def print_kwargs(**kwargs):
    print("Kwargs received:", kwargs)

print_kwargs(a=1, b=2, c=3)

#  Generator Functions
def number_generator():
    yield 1
    yield 2
    yield 3

gen = number_generator()
for num in gen:
    print("Generated:", num)

# Generator Expression
gen_exp = (x*x for x in range(4))
print("Generator expression values:")
for val in gen_exp:
    print(val)

#  Recursive Function (Factorial)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

#  Multi-type Return & Order of Args
def mixed_return(x, y):
    return x + y, x * y, x - y

sum_, product, diff = mixed_return(4, 2)
print("Sum:", sum_, "Product:", product, "Difference:", diff)

# Order of arguments
def all_args(a, b=10, *args, c, d=5, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, d={d}, kwargs={kwargs}")

all_args(1, 2, 3, 4, c=6, d=7, extra="test")