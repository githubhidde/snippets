import requests
import webbrowser

# Replace the following with the API key generated.

API_KEY = "guiSRRzgEQ6kEgjYICWXimV6Vy5BkvPk"

endpoint = "https://api.giphy.com/v1/gifs/search"

search_term = "mad"

params = {"api_key": API_KEY, "limit": 1, "q": search_term, "rating": "g"}

response = requests.get(endpoint, params=params).json()

for gif in response["data"]:

    title = gif["title"]

    trending_date = gif["trending_datetime"]

    url = gif["url"]

    print(f"{title} | {url}")

webbrowser.open(url)