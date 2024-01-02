from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.newegg.com/p/pl?d=graphics+cards"

# Opening up connection, grabbing the page
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

# Parse it as an HTML parse file
page_soup = BeautifulSoup(page_html, "html.parser")

# Grab each item
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "Position, Link \n"
f.write("")

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "/n")