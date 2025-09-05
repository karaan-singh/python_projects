import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    joke = response.json()
    print(f"{joke['setup']}\n{joke['punchline']}")
else:
    print("Could not fetch a joke at this time.")