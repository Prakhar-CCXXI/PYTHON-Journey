# import urllib.request , urllib.parse , urllib.error
#
# url = urllib.request.urlopen("http://127.0.0.1:8000/helloworld/")
#
# for line in url:
#     print(line.decode().strip())


import requests

url = "http://127.0.0.1:8000/helloworld/"
url2 = "http://127.0.0.1:8000/"


response = requests.get(url = url)
response2 = requests.get(url = url2 )

print(response) # Tells me whether the web.py file is connected to the website or not
print(dir(response)) # Returns me the function related to response
print(response.status_code) # Example use of functions . returns me the status code
print(response.headers) # Returns the headers
print(response.content) # Returns the content
print(type(response.content)) # Returns the content
print(type(response2.text)) # Returns the text

