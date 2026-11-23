import requests
from bs4 import BeautifulSoup 

def get_news(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (x11 ; Linux x86_64)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html.parser")
        newtitles = soup.find_all("h2")
        counter = 1 
        for title in newtitles[:10]:
            print(f"{counter}. {title.get_text(strip=True)}")
            counter += 1
    elif response.status_code == 404:
        print("Error 404: page not found")
    else : 
        print("unknown error ")

bbcurl = "https://www.bbc.com/news"
get_news(url=bbcurl)