import requests
from bs4 import BeautifulSoup
import pandas as pd

guelph_rental_url = "https://thecannon.ca/classified/housing/93144/"
HEADERS = {
"Accept": "*/*",
"Accept-encoding": "gzip, deflate, br, zstd",
"Accept-language": "en-US,en;q=0.9",
"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

#send a GET requests to the given URL
#page = requests.get("https://thecannon.ca/housing/page/1/")
#page = requests.get("https://books.toscrape.com/catalogue/page-1.html")

#Returns the raw HTML of the page
#print(page.text)

#Returns HTTP status code (200 = success)
#print(page.status_code)

#Converst HTML into a searchable object. 'html.parser' is the built-in parser
#soup = BeautifulSoup(page.text, "html.parser")

#print(soup.title.text)


current_page = 1

# where the data from the scraping is stored
data = []

#Just loop through the web until it false
while True:
    #just print the current page the scraping is on
    print("currently scraping page: "+str(current_page))

#The url where the information comes from
    url = "https://thecannon.ca/housing/page/"+str(current_page)+"/"
#This get the information from it
    page = requests.get(url)
    # Converst HTML into a searchable object. 'html.parser' is the built-in parser
    soup = BeautifulSoup(page.text, "html.parser")
#The Heading to help find all the information required
    all_rentals = soup.find_all("li", class_="housing-item")

    if not all_rentals:
        print("No more listing found. Stopping")
        break



    for house in all_rentals:
        title_tag = house.find("h2")
        link_tag = house.find("a")
        price_tag = house.find("li", class_="price")
        posted_tag = house.find("li", class_="post-date")
        description_tag = house.find("div", class_="description")
        item = {
            "Title":title_tag.find("a").text.strip() if title_tag else "N/A",
            "Link": link_tag.attrs["href"] if link_tag else "N/A",
            "Price":price_tag.find("dd").text.strip() if price_tag else "N/A",
            "Posted":posted_tag.find("dd").text.strip() if posted_tag else "N/A",
            "Description":description_tag.text.strip() if description_tag else "N/A"

        }


        data.append(item)

    current_page += 1

df = pd.DataFrame(data)

df.to_csv("houses.csv")