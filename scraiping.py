import requests
 
webpage_response = requests.get('https://www.goldmansachs.com/')
print(webpage_response.text)