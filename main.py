import pandas as pd
import streamlit as st
from clean_data import clean_data
import io

# Klares Ziel für heute: 

# ---> Finish & Push

# ---> Reflektieren 15 min 

def calc_sales_volume(df):
    df['Umsatz'] = df['Verkäufe'] * df['Preis']
    return df

def calculate_total_revenue(df):
    total = df['Umsatz'].sum()
    return total

def get_top_products(df, n=5):
    # Gesamtumsatz pro Produkt berechnen
    top_products = df.groupby('Produkt')['Umsatz'].sum().reset_index().sort_values(by='Umsatz', ascending=False)
    top_products = top_products.reset_index(drop=True).head(n)
    return top_products

def get_category_stats(df):
    stats = df.groupby('Kategorie').agg({'Umsatz': 'sum', 'Verkäufe': 'sum', 'Preis': 'mean'})
    stats.rename(columns={'Preis': 'Durchschnittspreis'}, inplace=True)
    return stats

# Füge st.bar_chart(monate) für visuelle Monatsanalyse hinzu
def months_analysis(df):
    # Daten in Monate aufteilen
    df['Jahr_Monat'] = df['Datum'].dt.to_period('M')
    months = df.groupby('Jahr_Monat')['Umsatz'].sum().reset_index()
    sorted_months = months.sort_values(by='Jahr_Monat').reset_index(drop=True)

    return sorted_months

def format_cash(value):
    # Zahl zu Geldbetrag formatieren
    if isinstance(value, pd.Series):
        return value.apply(lambda x: f'{x:,.2f} €')
    else: return f'{value:,.2f}'

def check_file_format(file):
    # Nur CSV-Datein akzeptieren
    if file:
        if not file.name.endswith('.csv'):
            st.warning('Dieses Dateiformat wird nicht unterstützt. Bitte lade eine CSV-Datei hoch.')
            return None
        else:
            return file
        

def generate_report():

    # ----- Streamlit UI -----
    st.markdown('# 📈 Sales Report Generator')
    st.markdown('---')

    # ---- Upload für Sales-Daten ----
    file = st.file_uploader('Sales-Daten', accept_multiple_files=False)
    file = check_file_format(file)
    st.markdown('---')
    # Ohne hochgeladene CSV: Demo-Daten verwenden
    if file is None:
        st.markdown('## Demo-Report')
        file = 'data/raw.csv'

    # Daten vorbereiten
    df = clean_data(file)
    df = calc_sales_volume(df)

    # Kategorie Filtern
    kategorien = list(df['Kategorie'].unique())
    kategorien.append('Alle Kategorien')
    auswahl = st.selectbox('Filtern', kategorien, index=3)

    # Nach gewählter Kategorie Filtern
    if auswahl != 'Alle Kategorien':
        df = df[df['Kategorie'] == auswahl]

    # Gesamtumsatz
    st.markdown('')
    st.markdown('')
    total = calculate_total_revenue(df)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.metric('Gesamtumsatz', value=format_cash(total))

    # ---- Top Produkte ----
    n = st.slider('Anzahl', min_value=0, max_value=df['Produkt'].nunique(), value=3)
    top_products = get_top_products(df, n)
    # Umsatz umformartieren für Anzeige
    top_products['Umsatz'] = format_cash(top_products['Umsatz'])
    st.markdown(f'#### Top {len(top_products)} Produkte')
    st.dataframe(top_products)

    st.markdown('---')

    # ---- Monatsanalyse ----
    st.markdown('#### Monatlicher Umsatz')
    months = months_analysis(df)
    # Period-Objekt für den Plot zu String formatieren
    months['Jahr_Monat'] = months['Jahr_Monat'].dt.strftime('%b-%Y')
    # Balkendiagramm
    st.bar_chart(months, x='Jahr_Monat', y='Umsatz', x_label='Monat', y_label='Umsatz (€)', sort=False)

    # ---- Kategorie Statistiken ----
    st.markdown('#### Kategorie Statistiken')
    stats = get_category_stats(df)
    # Geldbeträge für die Anzeige formatieren
    for col_name in ['Durchschnittspreis', 'Umsatz']:
        stats[col_name] = format_cash(stats[col_name])
    st.dataframe(stats)

    st.markdown('---')
        
    # Gesamten Report als Exel erstellen
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        top_products.to_excel(writer, sheet_name='Top Produkte', index=False)
        stats.to_excel(writer, sheet_name='Kategorien', index=False)
        months.to_excel(writer, sheet_name='Monate', index=False)

    st.download_button(
        label="📥 Kompletter Report (Excel)",
        data=buffer.getvalue(),
        file_name='sales_report.xlsx',
        mime='application/vnd.ms-excel',
        width='stretch'
    )


if __name__ == '__main__':
    generate_report()