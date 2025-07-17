import pandas as pd

# Path ke file kalender
KALENDER_PATH = "kalender_jawa_lengkap.csv"

# Load kalender sekali saja saat modul diimport
try:
    kalender_df = pd.read_csv(KALENDER_PATH, dtype=str)
    kalender_df["tanggal"] = kalender_df["tanggal"].str.strip()
except FileNotFoundError:
    kalender_df = pd.DataFrame()
    print(f"❌ File {KALENDER_PATH} tidak ditemukan.")

def lookup_kalender(tanggal_str):
    """
    Cari informasi hari, pasaran, dan neptu dari tanggal (format: dd/mm/yyyy)
    """
    if kalender_df.empty:
        raise ValueError("Data kalender tidak tersedia.")

    tanggal_str = tanggal_str.strip()
    row = kalender_df[kalender_df["tanggal"] == tanggal_str]

    if row.empty:
        raise ValueError("Tanggal tidak ditemukan di data kalender.")

    result = {
        "hari": row.iloc[0]["hari"],
        "pasaran": row.iloc[0]["pasaran"],
        "neptu_hari": int(row.iloc[0]["neptu_hari"]),
        "neptu_pasaran": int(row.iloc[0]["neptu_pasaran"]),
        "neptu_jumlah": int(row.iloc[0]["neptu_jumlah"]),
    }
    return result
