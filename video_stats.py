import requests
import json
API_KEY = 'AIzaSyCDU3lPUdWltkpvCw2BZwYrJXi0rYnbwM0'
Channel = 'MrBeast'
url = f'https://youtube.googleapis.com/youtube/v3/channels?part=ContentDetails&forHandle={Channel}&key= {API_KEY}'
response = requests.get(url)

print(response)

data = response.json()
print(json.dumps(data, indent = 4))

channel_item = data['items'][0]
channel_id = channel_item['contentDetails']['relatedPlaylists']['uploads']
print(channel_id)