import requests
import json

url = "https://newsapi.org/v2/everything?pageSize=5&q=crypto&apiKey=cc5426462a664c0399c218ae0bdfd1b9"

# Fetch the JSON data from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Decode the JSON data
    data = json.loads(response.text)

    urls = []
    for article in data['articles']:
        urls.append(article['url'])

    for url in urls:
        print(url)
else:
    print("Error fetching data: ", response.status_code)
