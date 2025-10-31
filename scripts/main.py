import json
import os

import pandas as pd
import requests
from decorators import artist_decorator
from frontend import *

API_URL = "https://www.theaudiodb.com/api/v1/json"
API_test_key = "/123"
API_URL_with_key = API_URL + API_test_key

if not os.path.exists("artists"):
    os.mkdir("artists")
    print("Created folder 'artists'")
else:
    pass


@artist_decorator
def get_artist_generell_info(artist: str):
    request = requests.get(
        f"https://www.theaudiodb.com/api/v1/json/123/search.php?s={artist}"
    )
    with open(f"artists/{artist}.json", "w", encoding="UTF-8") as r:
        actual_json = request.json()
        json_dumped = json.dumps(actual_json)
        r.write(json_dumped)
        df = pd.json_normalize(actual_json, "artists")
        website = df["strWebsite"]
        print(list(website))


def main():
    # NUR: Artist aus dem Fenster nehmen statt input()
    artist = (values.get("-ARTIST-", "") if values else "").strip()
    if artist:
        get_artist_generell_info(artist)


if __name__ == "__main__":
    main()
