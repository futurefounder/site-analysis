import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

# Funktion zum Abrufen und Parsen der Sitemap
def sitemap_to_csv(sitemap_url, output_file=None):
    try:
        # Sitemap abrufen
        response = requests.get(sitemap_url)
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Sitemap. Statuscode: {response.status_code}")
            return
        
        # Sitemap mit BeautifulSoup parsen
        soup = BeautifulSoup(response.content, "xml")
        url_tags = soup.find_all("url")
        
        # URLs und "lastmod"-Metadaten extrahieren
        data = []
        for url_tag in url_tags:
            loc = url_tag.find("loc").text if url_tag.find("loc") else None
            lastmod = url_tag.find("lastmod").text if url_tag.find("lastmod") else None
            
            data.append({
                "URL": loc,
                "Last Modified": lastmod
            })
        
        # In DataFrame umwandeln
        df = pd.DataFrame(data)
        
        # Output-Dateiname generieren, falls nicht angegeben
        if not output_file:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_file = f"{current_time}_sitemap.csv"
        
        # In CSV exportieren
        df.to_csv(output_file, index=False)
        print(f"Sitemap erfolgreich in '{output_file}' gespeichert.")
    
    except Exception as e:
        print(f"Fehler beim Verarbeiten der Sitemap: {e}")

# Beispielaufruf
sitemap_url = "https://www.nabu.de/sitemap.xml"  # Ersetze mit der URL deiner Sitemap
sitemap_to_csv(sitemap_url)
