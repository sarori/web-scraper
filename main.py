import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.fr/emplois?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=Nanterre+(92)&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
pagination = indeed_soup.find("div", {"class" : "pagination"})

pages = pagination.find_all('a')

spans = []
for page in pages:
    spans.append(page.find("span"))
spans = spans[:-1]
