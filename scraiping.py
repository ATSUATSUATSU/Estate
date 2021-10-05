import requests
 
webpage = requests.get('https://www.goldmansachs.com/')
print(webpage.text)