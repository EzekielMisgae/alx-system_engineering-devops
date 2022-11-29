import requests


data = requests.get('https://www.reddit.com/r/programming/hot/.json', headers={'User-Agent': "subscribers"})

print(data.json().get("data").get('children'))
n = data.json().get("data").get('children')

print(len(n))