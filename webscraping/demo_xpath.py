import httpx
import lxml.html

# first we'll fetch the HTML in question and load it with lxml
response = httpx.get("https://www.senate.gov/senators/SenateSalariesSince1789.htm")
root = lxml.html.fromstring(response.text)

rows = root.xpath("//table[@id='SortableData_table']/tbody/tr")
for row in rows:
    # like above, we start our query now on the row in question (not root)
    # and use Xpath's directory-like syntax to get the underlying text
    year_td, salary_td = row.xpath(".//td")
    year = year_td.text_content()
    salary = salary_td.text_content()
    print(year, "|", salary)
