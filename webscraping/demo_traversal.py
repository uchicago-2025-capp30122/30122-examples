import httpx
import lxml.html

# first we'll fetch the HTML in question and load it with lxml
response = httpx.get("https://www.senate.gov/senators/SenateSalariesSince1789.htm")
root = lxml.html.fromstring(response.text)

print(root)

print("\n------\n")

# we can examine the root node and see 3 children
print("children", root.getchildren())

print("\n------\n")

# but it'll be more reliable to jump straight to the table by ID
table = root.get_element_by_id("SortableData_table")
print("Children of table:", table.getchildren())
print("Rows: ", table.getchildren()[2].getchildren())
