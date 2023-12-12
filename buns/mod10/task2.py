import requests
import re

def get_subtitles(url):
  response = requests.get(url)
  if response.status_code == 200:
    subtitles = re.findall(r'
    (.*?)
    ', response.text)
    return subtitles
  else:
    return []

url = 'http://example.com/sample-web-page'
subtitles = get_subtitles(url)
print(subtitles)
