import requests

headers = {"User-Agent": "TourTourTouri/2.0 (EVM x8), CurlyLegs40/1;p"}


s = requests.Session()
s.headers.update(headers)
base_url = "url for searched keyword"

to_file = s.get(base_url)

with open(f"filename.html", "w") as f:
    f.write(to_file.text)
