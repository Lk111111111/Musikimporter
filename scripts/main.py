import json
import os
import webbrowser

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

APP_NAME = "Musikimporter"


def get_audius_host():
    try:
        r = requests.get("https://api.audius.co", timeout=10)
        r.raise_for_status()
        hosts = r.json().get("data") or []
        return hosts[0] if hosts else None
    except Exception as e:
        print("Audius host fetch failed:", e)
        return None


def audius_search_tracks(host, artist, limit=15):
    if not host or not artist:
        return []
    try:
        r = requests.get(
            f"{host}/v1/tracks/search",
            params={
                "query": artist,
                "limit": limit,
                "app_name": APP_NAME,
                "sort_method": "popular",
            },
            timeout=15,
        )
        r.raise_for_status()
        return r.json().get("data") or []
    except Exception as e:
        print("Audius search error:", e)
        return []


def audius_stream_url(host, track_id):
    if not host or not track_id:
        return None
    return f"{host}/v1/tracks/{track_id}/stream?app_name={APP_NAME}"


@artist_decorator
def get_artist_generell_info(artist: str):
    """Gets short description of The Artist from theaudiodb"""
    request = requests.get(
        f"https://www.theaudiodb.com/api/v1/json/123/search.php?s={artist}"
    )
    actual_json = request.json()
    with open(f"artists/{artist}.json", "w", encoding="UTF-8") as r:
        json_dumped = json.dumps(actual_json)
        r.write(json_dumped)

    # Safely handle cases where artists is None or empty
    artists_list = (actual_json or {}).get("artists") or []
    if not artists_list:
        print("No artist found on TheAudioDB")
        return

    df = pd.json_normalize(artists_list)
    website_series = df.get("strWebsite")
    if website_series is None or website_series.dropna().empty:
        print("No Website found")
    else:
        print(website_series.dropna().tolist())


def main(values_param=None):
    vals = values_param or values
    artist = (vals.get("-ARTIST-", "") if vals else "").strip()
    if not artist:
        print("No artist entered")
        return

    get_artist_generell_info(artist)

    host = get_audius_host()
    if not host:
        print("Could not get an Audius host.")
        return
    print("Using Audius host:", host)

    tracks = audius_search_tracks(host, artist, limit=15)
    if not tracks:
        print("No Audius results for:", artist)
        return

    # Show a small list in the console
    for i, t in enumerate(tracks, 1):
        title = t.get("title", "(untitled)")
        user = (t.get("user") or {}).get("name", "Unknown Artist")
        print(f"{i}. {title} — {user}")
    selection = True
    while selection:
        try:
            song_selection = (
                int(input("What song do you want to listen to from this top 15: ")) - 1
            )
            song = tracks[song_selection]
        except (ValueError, IndexError):
            print("Please enter a valid number between 1 and", len(tracks))
            continue

        url = audius_stream_url(host, song.get("id"))
        if url:
            print("Opening stream:", url)
            webbrowser.open(url)
        else:
            print("Could not build stream URL.")

        user_choice_to_continue_next_artist_or_stay = (
            input(
                "Do you wish to play more from this list (True) or search a new artist (False)? : "
            )
            .strip()
            .lower()
        )

        if user_choice_to_continue_next_artist_or_stay in (
            "false",
            "f",
            "no",
            "n",
            "0",
        ):
            break


if __name__ == "__main__":
    main()
