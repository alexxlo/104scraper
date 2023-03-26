import requests

headers = {"User-Agent": "TourTourTouri/2.0 (EVM x8), CurlyLegs40/1;p"}


s = requests.Session()
s.headers.update(headers)
base_url = "https://www.104.com.tw/jobs/search/?keyword=%E7%88%AC%E8%9F%B2%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0"

to_file = s.get(base_url)

with open(f"vacancies.html", "w") as f:
    f.write(to_file.text)