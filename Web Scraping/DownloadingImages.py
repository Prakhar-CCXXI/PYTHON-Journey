import requests
import re

user = input("Enter the image name: ")
useragent = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"

}

url = f"https://www.google.com/search?sca_esv=144b6c23fea26314&sxsrf=AE3TifNXUXu04JBI-Cf7Y0xpTHqBPg17_w:1759939720257&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEheAY38UjnRKVLYFDREDmz6ZuF5vGKadO4eyTxfJeUAUMG824jBAJyyOFku2EE6yFAMG92rVlgj_vAxQXNB1YTKi5vnFC7sIzwBMMxojLsnnE1TcdECqxzRobFhi6gbOmGGyvyA&q={user}&sa=X&ved=2ahUKEwiRkuiu_pSQAxVmla8BHd8IKdYQtKgLegQIDxAB&biw=1536&bih=778&dpr=1.25"

response = requests.get(url = url , headers = useragent).text

pattern = r'https://www\.google\.com/search\?[^"\s]+'



images = re.findall(pattern , response)

for image in images:
    print(eval(image))


#https://www.google.com/search?sca_esv=144b6c23fea26314&amp;sxsrf=AE3TifNXUXu04JBI-Cf7Y0xpTHqBPg17_w:1759939720257&amp;udm=2&amp;fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEheAY38UjnRKVLYFDREDmz6ZuF5vGKadO4eyTxfJeUAUMG824jBAJyyOFku2EE6yFAMG92rVlgj_vAxQXNB1YTKi5vnFC7sIzwBMMxojLsnnE1TcdECqxzRobFhi6gbOmGGyvyA&amp;q=moon&amp;sa=X&amp;ved=2ahUKEwiRkuiu_pSQAxVmla8BHd8IKdYQtKgLegQIDxAB&amp;biw=1536&amp;bih=778&amp;dpr=1.25