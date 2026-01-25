import pandas as pd

def clean_data(data):
    df = pd.read_csv(data, encoding='utf-8', sep=',', header=0)
    df = df.dropna()
    # Datum parsen
    df['Datum'] = pd.to_datetime(df['Datum'], format='%Y-%m-%d', errors='raise')
    return df