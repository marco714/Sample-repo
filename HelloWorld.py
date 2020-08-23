import math
import sys
from os import rename

import requests


r = request.get("https://coreyms.com")
print("Changes Here")
print(r.status_code)
print(r.ok)

def divide_func(x, y):
    return x / y

result = divide_func(6,3)