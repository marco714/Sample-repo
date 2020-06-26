import math
import sys
from os import rename

import requests


r = request.get("https://coreyms.com")
print(r.status_code)
print(r.ok)