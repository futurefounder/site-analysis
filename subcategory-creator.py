import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from tqdm import tqdm
from urllib.parse import urlparse

# Sitemap-CSV laden
sitemap_file = "2024-11-15_11-27-33_sitemap.csv"  # Ersetze mit deinem Dateinamen
df_sitemap = pd.read_csv(sitemap_file)

# Datenstruktur für Subkategorien
subcategories = []

# Hierarchien aus allen URLs in der Sitemap extrahieren
print("Starte die Analyse der Subkategorien für die gesamte Sitemap...\n")
for index, row in tqdm(df_sitemap.iterrows(), total=df_sitemap.shape[0], desc="Verarbeitung der Sitemap-URLs"):
    url = row["URL"]
    try:
        # HTML-Seite abrufen
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Links finden, die zu weiteren Kategorien führen könnten
            links = soup.find_all("a", href=True)
            for link in links:
                href = link["href"]
                # Filter links that start with the base path and ignore root or empty paths
                if href.startswith("/") and not href.endswith("/"):

                    # Erstellen der vollständigen URL für die gefundenen Subkategorien
                    full_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}{href}"

                    # Hierarchie aus URL extrahieren
                    path_parts = href.strip("/").split("/")
                    hierarchy = {
                        "Full URL": full_url,
                        "Parent URL": url,
                    }
                    for level, part in enumerate(path_parts):
                        hierarchy[f"Level {level + 1}"] = part

                    subcategories.append(hierarchy)
    except Exception as e:
        print(f"Fehler beim Verarbeiten von {url}: {e}")

# In DataFrame umwandeln
df_subcategories = pd.DataFrame(subcategories)

# CSV-Dateiname erstellen
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{current_time}_full_sitemap_subcategories_with_hierarchy.csv"

# Ergebnisse speichern
df_subcategories.to_csv(filename, index=False)

print(f"\nDie Subkategorien mit Hierarchie für die gesamte Sitemap wurden erfolgreich in der Datei '{filename}' gespeichert.")
