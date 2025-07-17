from datetime import datetime

def hitung_weton(tanggal):
    # Pastikan input berupa datetime, bukan string
    if isinstance(tanggal, str):
        try:
            tanggal = datetime.strptime(tanggal, "%d/%m/%Y")
        except ValueError:
            return {
                'error': 'Format tanggal salah. Gunakan format DD/MM/YYYY.'
            }

    # Daftar pasaran dan neptu-nya
    pasaran = ['Legi', 'Pahing', 'Pon', 'Wage', 'Kliwon']
    neptu_pasaran = [5, 9, 7, 4, 8]

    # Daftar hari dan neptu-nya
    hari = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    neptu_hari = [5, 4, 3, 7, 8, 6, 9]

    # Hitung jumlah hari dari tanggal dasar
    delta_hari = (tanggal - datetime(1800, 1, 1)).days

    index_pasaran = delta_hari % 5
    index_hari = tanggal.weekday()  # Senin = 0, Minggu = 6

    hari_jawa = hari[(index_hari + 1) % 7]  # konversi ke format Jawa
    pasaran_jawa = pasaran[index_pasaran]
    neptu = neptu_hari[(index_hari + 1) % 7] + neptu_pasaran[index_pasaran]

    return {
        'tanggal': tanggal.strftime("%A, %d %B %Y"),
        'hari': hari_jawa,
        'pasaran': pasaran_jawa,
        'neptu': neptu
    }
