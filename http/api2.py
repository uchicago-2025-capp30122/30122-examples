# API Example 2: use more httpx features
import httpx
from pprint import pprint

url = "https://api.fda.gov/food/enforcement.json"

# let library generate query string
# gives us an easier format to work with
params = {"search": "distribution_pattern:nationwide", "limit": 2}

response = httpx.get(url, params=params)
# response objects have built in .json() method for decoding
pprint(response.json())
