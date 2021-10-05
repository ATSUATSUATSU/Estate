import requests
 
webpage_response = requests.get('https://www.goldmansachs.com/')
print(webpage_response.text)




import requests
from bs4 import BeautifulSoup

##webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
webpage_response = requests.get('https://www.goldmansachs.com/')


webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

print(soup)