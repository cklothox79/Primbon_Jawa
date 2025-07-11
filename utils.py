# utils.py
from datetime import datetime

pasaran = ['Legi', 'Pahing', 'Pon', 'Wage', 'Kliwon']
neptu_pasaran = {'Legi': 5, 'Pahing': 9, 'Pon': 7, 'Wage': 4, 'Kliwon': 8}
neptu_hari = {'Senin': 4, 'Selasa': 3, 'Rabu': 7, 'Kamis': 8, 'Jumat': 6, 'Sabtu': 9, 'Minggu': 5}

def hitung_weton(tanggal):
    hari = tanggal.strftime('%A')
    delta_hari = (tanggal - datetime(1800, 1, 1)).days
    pasaran_index = delta_hari % 5
    pasaran_hari = pasaran[pasaran_index]
    
    total_neptu = neptu_hari[hari] + neptu_pasaran[pasaran_hari]
    
    # Contoh sifat berdasarkan neptu
    sifat = "Bijaksana" if total_neptu > 15 else "Sederhana"
    
    return {
        "weton": f"{hari} {pasaran_hari}",
        "neptu": total_neptu,
        "sifat": sifat
    }
