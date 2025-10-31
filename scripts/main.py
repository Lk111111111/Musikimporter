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
    """Gets short description of The Artist from theaudiodb

    Args:
        artist (str): name of the artist entered in the GUI
    """
    request = requests.get(
        f"https://www.theaudiodb.com/api/v1/json/123/search.php?s={artist}"
    )
    with open(f"artists/{artist}.json", "w", encoding="UTF-8") as r:
        actual_json = request.json()
        json_dumped = json.dumps(actual_json)
        r.write(json_dumped)
        df = pd.json_normalize(actual_json, "artists")
        website = df["strWebsite"]
        if list(website) == []:
            print("No Website found")
        else:
            print(list(website))


def main():
    """For now gets the artist value from GUI"""
    artist = (values.get("-ARTIST-", "") if values else "").strip()
    if artist:
        get_artist_generell_info(artist)
    else:
        print("No artist entered")


if __name__ == "__main__":
    main()
