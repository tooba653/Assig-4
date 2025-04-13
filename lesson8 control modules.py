# Built-in Module Example
import math
print("Square root using math module:", math.sqrt(16))

# User-defined Module
import my_module
my_module.hello()

# External Module 
import requests
response = requests.get("https://api.github.com")
print(response.status_code)


import math  # Basic Import
import math as m  # Import with alias
from math import pi, sqrt  # Specific imports
from math import *  # Import everything 