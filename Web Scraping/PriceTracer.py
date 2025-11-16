import requests
from bs4 import BeautifulSoup


class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
        self.response = requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response , "lxml")

    def product_title(self):
        title = self.soup.find("span",{"class":"shortcut-key nav-assistant-card-font font-color"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not Found"

    def product_price(self):
        price = self.soup.find("span",{"class":"a-offscreen"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not found"


device = PriceTracer(url="https://www.amazon.in/dp/B0DGSXWZ4G/?_encoding=UTF8&ref_=cct_cg_Mayart25_2b1&pf_rd_p=0bc22772-7d26-4092-b109-dcd587dd71b2&pf_rd_r=NC5C3CTXT3V2DF4SNYP4&th=1")
print(device.product_title())
print(device.product_price())