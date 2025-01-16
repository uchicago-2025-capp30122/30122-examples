# API example 1: simple usage
import httpx
import json
from pprint import pprint

# entire URL as a string
url = (
    "https://api.fda.gov/food/enforcement.json"
    "?search=distribution_pattern:nationwide&limit=2"
)
response = httpx.get(url)

# load JSON manually
data = json.loads(response.text)

pprint(data)
