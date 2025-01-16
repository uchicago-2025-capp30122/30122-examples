# API Example 3: Pagination (DO NOT RUN)
import httpx

raise Exception("do not run")

url = "https://api.fda.gov/food/enforcement.json"
limit = 10
skip = 0
results = []

while skip < 100:
    params = {"search": "distribution_pattern:nationwide", "limit": limit, "skip": skip}
    print(f"Fetching {url} {params}")
    response = httpx.get(url, params=params)
    results += response.json()["results"]
    skip += limit

print(f"obtained {len(results)} results")
