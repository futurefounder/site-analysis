# NABU Webseitenanalyse

Dieses Repository enthält Python-Scripts zur Analyse der Webseitenstruktur von nabu.de. Die Analyse wurde im Rahmen eines Universitätsprojekts zur Informationsarchitektur durchgeführt.

## Scripts und ihre Funktionen

### 1. sitemap-to-csv.py

- Lädt die XML-Sitemap von nabu.de
- Extrahiert URLs und "Last Modified"-Daten
- Speichert die Informationen in einer CSV-Datei
- Output: `YYYY-MM-DD_HH-MM-SS_sitemap.csv`

### 2. subcategory-creator.py

- Analysiert die URLs aus der Sitemap
- Extrahiert Hierarchieebenen der Webseite
- Erstellt vollständige URLs für Subkategorien
- Output: `YYYY-MM-DD_HH-MM-SS_full_sitemap_subcategories_with_hierarchy.csv`

### 3. classifications_analysis.py

- Extrahiert Kategorien von der NABU-Hauptseite
- Verwendet BeautifulSoup für HTML-Parsing
- Speichert Kategorie-Namen und Links
- Output: `YYYY-MM-DD_HH-MM-SS_categories.csv`

### 4. remove_ded.py

- Entfernt Duplikate aus den Subkategorien
- Bereinigt URLs von HTML-Endungen
- Erstellt eindeutige Kategoriepfade
- Output: `YYYY-MM-DD_HH-MM-SS_unique_subcategories.csv`

## Vorgehensweise

1. Sitemap-Analyse

   - Abruf der XML-Sitemap mit `sitemap-to-csv.py`
   - Erste Übersicht über alle URLs der Webseite

2. Hierarchie-Extraktion

   - Verarbeitung der Sitemap-Daten mit `subcategory-creator.py`
   - Identifikation der Webseitenstruktur

3. Kategorisierung

   - Analyse der Hauptkategorien mit `classifications_analysis.py`
   - Extraktion der Navigationselemente

4. Bereinigung
   - Deduplizierung der Daten mit `remove_ded.py`
   - Erstellung einer übersichtlichen Kategoriestruktur

## Verwendete Tools und KI-Unterstützung

- **Skript-Entwicklung**: ChatGPT wurde für die initiale Entwicklung der Python-Scripts verwendet
- **README-Erstellung**: Dieses README wurde mit Unterstützung von Claude (Anthropic) erstellt
- **Haupttechnologien**: Python, BeautifulSoup4, Pandas

## Ergebnisse

Die Analyse ergab, dass etwa 89% der Inhalte auf nabu.de sich mit dem Thema Vögel beschäftigen, was die thematische Schwerpunktsetzung der Website verdeutlicht.

## Voraussetzungen

```bash
pip install requests beautifulsoup4 pandas tqdm
```
