# Import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Print attributes of all the a elements
for a in soup.find_all("a"):
  print(a.attrs)

# Print only the text of all the p tags
for p in soup.find_all("p"):
  print(p.get_text())