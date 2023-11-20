import requests
import json

api_key = 'acc_4b32583a2ba9a5d'
api_secret = '118f7df0cd2b4d7ff9f2ee6235bb8561'
image_url = 'https://worldanimalfoundation.org/wp-content/uploads/2023/10/types-of-huskies-2.jpg'
langs = 'en,es'

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s&language=%s' % (
        image_url, langs),
    auth=(api_key, api_secret)
)
data = response.json()

for tag in data["result"]["tags"]:
    print(tag)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
