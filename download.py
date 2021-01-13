import sys
import os

import pandas as pd
import requests

url = "https://theodorepayne.org/plants-and-seeds/nursery/inventory/"
headers = {"User-agent": os.environ["CONTACT_INFO"]}
html = requests.get(url, headers=headers).text
pd.read_html(html, header=0)[0].to_csv("data.csv", index=False)
