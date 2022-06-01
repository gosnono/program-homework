import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.nongmin.com"
    res = requests.get("http://www.nongmin.com/news/NEWS/NEW/list")
    soup = BeautifulSoup(res.content)
    res.close()

    find_str = soup.find("div", attrs={"class": "card_type03"})

    for news  in find_str.findAll('div', attrs={'class': '_contentRoot'})

    print(find_str)

if __name__ == "__main__":
    main()

