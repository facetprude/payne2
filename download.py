import os

import pandas as pd
import requests

url = "https://theodorepayne.org/plants-and-seeds/nursery/inventory/"
CONTACT_INFO = os.environ["CONTACT_INFO"]
if not CONTACT_INFO:
    raise ValueError('No contact information set. Set $CONTACT_INFO.')

headers = {"User-agent": CONTACT_INFO}
html = requests.get(url, headers=headers).text
pd.read_html(html, header=0)[0].to_csv("data.csv", index=False)
