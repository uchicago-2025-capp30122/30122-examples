import httpx
import lxml.html

# first we'll fetch the HTML in question and load it with lxml
response = httpx.get("https://www.senate.gov/senators/SenateSalariesSince1789.htm")
root = lxml.html.fromstring(response.text)

# Ideally, we would rely less on getchildren() since a change to the
# structure would break our scraper.
# Here we use a CSS Selector:
#
#    #SortableData_table   -- the # character looks up by ID
#    tbody tr              -- names without a leading # or . refer to tag names
#
# So this grabs "all tr elements that are inside the tbody
#  that are inside id=SortableData_table".
rows = root.cssselect("#SortableData_table tbody tr")
for row in rows:
    # this time we'll iterate over the <td> elements within
    # since we are starting the .cssselect with `row` instead of `root`
    # this only gets the <td>s within the current row
    year_td, salary_td = row.cssselect("td")

    # finally, we use .text_content() to extract the text nodes
    # which contain the data we're after
    year = year_td.text_content()
    salary = salary_td.text_content()
    print(year, "|", salary)
