import os
import requests

url = 'https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20210001177/U/D20211177Lj.pdf'

many_urls = ['https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20000941037/U/D20001037Lj.pdf',
             'https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20040540535/U/D20040535Lj.pdf'
             ]

location = "C:/Users/kulic/OneDrive/Bureau/save_here/file.pdf"

# Pobieranie pliku z internetu
response = requests.get(url)

# Sprawdzanie, czy pobranie zakończyło się sukcesem
if response.status_code == 200:
    with open(location, 'wb') as file:
        file.write(response.content)
    print(f"file downloaded and saved under location: {location}")
else:
    print(f"unable to save file. response status code: {response.status_code}")

