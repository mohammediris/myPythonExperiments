
import requests

response = requests.get('https://www.youtube.com')
if response.status_code == 200:
    print("website is working")
else:
    print("website not working")