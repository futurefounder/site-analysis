import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL der Webseite
url = "https://www.nabu.de/tiere-und-pflanzen/index.html"

# Webseite abrufen
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Kategorien extrahieren (z.B. anhand von CSS-Klassen oder HTML-Tags)
categories = soup.find_all("a", class_="teaser-title")  # Beispiel für Links mit Kategorie-Namen

# Daten strukturieren
data = []
for cat in categories:
    category_name = cat.get_text(strip=True)
    link = cat['href'] if 'href' in cat.attrs else None
    data.append({"Category": category_name, "Link": link})

# In DataFrame speichern
df = pd.DataFrame(data)

# Dateiname mit Datum und Uhrzeit erstellen (Datum zuerst)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{current_time}_categories.csv"

# Ergebnisse in eine CSV exportieren
df.to_csv(filename, index=False)

print(f"Die Daten wurden in der Datei '{filename}' gespeichert.")
