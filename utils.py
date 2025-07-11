from datetime import datetime
import pandas as pd

pasaran = ['Legi', 'Pahing', 'Pon', 'Wage', 'Kliwon']
neptu_pasaran = {'Legi': 5, 'Pahing': 9, 'Pon': 7, 'Wage': 4, 'Kliwon': 8}
neptu_hari = {'Senin': 4, 'Selasa': 3, 'Rabu': 7, 'Kamis': 8, 'Jumat': 6, 'Sabtu': 9, 'Minggu': 5}

def hitung_weton(tanggal):
    hari = tanggal.strftime('%A')
    delta_hari = (tanggal - datetime(1800, 1, 1)).days
    pasaran_index = delta_hari % 5
    pasaran_hari = pasaran[pasaran_index]
    total_neptu = neptu_hari[hari] + neptu_pasaran[pasaran_hari]
    sifat = "Bijaksana" if total_neptu >= 15 else "Sederhana"
    return {
        "weton": f"{hari} {pasaran_hari}",
        "neptu": total_neptu,
        "sifat": sifat
    }

def cari_jodoh(weton1, weton2):
    try:
        hari1, pasar1 = weton1.split()
        hari2, pasar2 = weton2.split()
        neptu1 = neptu_hari[hari1] + neptu_pasaran[pasar1]
        neptu2 = neptu_hari[hari2] + neptu_pasaran[pasar2]
        total = neptu1 + neptu2
        if total in range(20, 25):
            return "Sangat Serasi"
        elif total in range(25, 30):
            return "Cukup Serasi"
        else:
            return "Kurang Serasi"
    except:
        return "Format weton salah. Gunakan format: Senin Kliwon"

def tafsir_mimpi(mimpi):
    try:
        df = pd.read_csv("data/mimpi.csv")
        hasil = df[df["mimpi"].str.contains(mimpi, case=False)]
        if not hasil.empty:
            return hasil.iloc[0]["arti"]
        else:
            return "Tidak ditemukan arti mimpi tersebut."
    except:
        return "Data mimpi belum tersedia."
