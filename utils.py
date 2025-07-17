import pandas as pd
from datetime import datetime

# Load kalender Jawa dari file CSV
kalender_df = pd.read_csv("kalender_jawa.csv")

def lookup_kalender(tanggal_str):
    # Format input: dd/mm/yyyy
    tanggal = datetime.strptime(tanggal_str, "%d/%m/%Y").date()
    tanggal_formatted = tanggal.strftime("%Y-%m-%d")

    row = kalender_df[kalender_df['tanggal'] == tanggal_formatted]
    if row.empty:
        raise ValueError("Tanggal tidak ditemukan di data kalender")

    hari = row.iloc[0]['hari']
    pasaran = row.iloc[0]['pasaran']
    neptu = int(row.iloc[0]['neptu'])

    return {
        "tanggal": tanggal_formatted,
        "hari": hari,
        "pasaran": pasaran,
        "neptu": neptu
    }
