import requests
import json
API_URL = "https://www.theaudiodb.com/api/v1/json"
API_test_key = "/123"
API_URL_with_key = API_URL+API_test_key

request = requests.get("https://www.theaudiodb.com/api/v1/json/123/search.php?s=coldplay")
with open("response.json", "w", encoding="UTF-8") as r:
    json_dumped = json.dumps(request.json())
    r.write(json_dumped)