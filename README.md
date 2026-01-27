
# 📈 Sales Report Generator

Ein schlankes **Streamlit-Tool** zur Analyse von Verkaufsdaten: CSV hochladen, automatisch bereinigen, Umsatz berechnen, Insights generieren und als Excel-Report exportieren.

---

## 🚀 Features

- 📂 CSV Upload oder Demo-Daten  
- 💰 Automatische Umsatzberechnung (Preis × Verkäufe)  
- 🏆 Top Produkte Analyse  
- 📊 Monatlicher Umsatz als Balkendiagramm  
- 🗂 Kategorie-Statistiken  
- 📄 Export als Excel-Report (mehrere Sheets)  

---

## 📝 Erwartetes CSV-Format

**Beispiel:**



Datum,Produkt,Kategorie,Preis,Verkäufe
2025-10-23,iPhone,Elektronik,999.99,3

````

**Spaltenbeschreibung:**

- **Datum** – Datum des Verkaufs  
- **Produkt** – Name des Produkts  
- **Kategorie** – Produktkategorie  
- **Preis** – Preis pro Einheit  
- **Verkäufe** – Anzahl der Verkäufe  

---

## ⚙️ Installation

**Repository klonen:**

```bash
git clone <repo-url>
cd sales-report-generator
````

**Dependencies installieren:**

```bash
pip install -r requirements.txt
```

Falls kein `requirements.txt` existiert:

```bash
pip install streamlit pandas xlsxwriter
```

---

## ▶️ Starten

```bash
streamlit run main.py
```

Der Browser öffnet automatisch: [http://localhost:8501](http://localhost:8501)

---

## 🛠 Funktionen

* `clean_data()` – Datenbereinigung
* `calc_sales_volume()` – Umsatz berechnen
* `get_top_products()` – Top N Produkte
* `months_analysis()` – Monatsumsatz
* `get_category_stats()` – Kategorie-Aggregate

---

## 📊 Excel Export

* **Top Produkte** – Umsatzstärkste Produkte
* **Kategorien** – Aggregierte Kategorie-Statistiken
* **Monate** – Monatliche Umsätze

---

## 💡 Optional

* Demo-Daten für erste Tests verfügbar
* Interaktive Streamlit Widgets für Filter nutzen
* Balkendiagramme und Pivot-Tabellen für bessere Visualisierung

