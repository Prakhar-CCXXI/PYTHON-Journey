import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")  # Use "lxml" only if installed

        first_div = soup.find("div")

        if first_div:
            # print(first_div.prettify())
            # h = first_div.find("a")
            # h = first_div.find("a").find("span")
            h = first_div.find_all("a")
            # print(h)
            content = [span.text for span in h ]
            print(content)

            with open("wiki.csv" , "w") as csv_file:
                csv_write = csv.writer(csv_file)
                csv_write.writerow(content)

        else:
            print("No <div> tag found.")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")

Extract("https://en.wikipedia.org/wiki/Universe")
