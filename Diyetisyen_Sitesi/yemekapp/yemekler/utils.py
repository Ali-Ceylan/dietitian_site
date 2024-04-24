import requests
from bs4 import BeautifulSoup

def get_link_data(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    tarif_adi = soup.find("h1", {"class":"recipe-detail-header__title"}).get_text()

    tarif_aciklama = soup.find("div", {"class":"recipe-description__content"}).get
   
    tarif_resim = soup.find('img', {'alt':'imageMissing Alt Text'}).parent.find('source')['srcset']
    
    return tarif_adi, tarif_aciklama, tarif_resim