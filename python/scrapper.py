import requests
from bs4 import BeautifulSoup
import bs4

keyword = "회계직원"
response=requests.get(
    f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0")

print(response)

soup = BeautifulSoup(response.text, "html.parser")

print(soup)
soup.find_all("li", class_="c_col")
print(lis)

jobs = [
    {"title" : "회계직원 모집", "company": "자연속애영농조합법인", "location" : "전남_화순군"}
]

for li in lis:
    company = li.find("a", class_="cpname").text
    title = li.find("div", class_="cell_mid").find("a").text
    location = li,find("div", class_="cell_mid").find_all("span")[3].text
    link = li.find("div", class_="cell_mid").find("a").get("href")

    job_data = {
        "title" : title,
          "company": company, 
          "location" :location,
          "link" : link

    }


