import requests
import json
API_URL = "https://www.theaudiodb.com/api/v1/json"
API_test_key = "/123"
API_URL_with_key = API_URL+API_test_key


def decorator(function):
    def wrapper(*args, **kwargs):
        function(artist)
        print("artist file created")
    return wrapper

@decorator
def get_artist_generell_info(artist: str):
    request = requests.get(f"https://www.theaudiodb.com/api/v1/json/123/search.php?s={artist}")
    with open(f"{artist}.json", "w", encoding="UTF-8") as r:
        json_dumped = json.dumps(request.json())
        r.write(json_dumped)

artist = input("Enter the artist to search for: ")
get_artist_generell_info(artist.strip())