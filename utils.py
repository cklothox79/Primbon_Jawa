import pandas as pd
from datetime import datetime

def lookup_kalender_jawa(tanggal, path_csv="kalender_jawa.csv"):
    try:
        df = pd.read_csv(path_csv)
        df['tanggal'] = pd.to_datetime(df['tanggal'], dayfirst=True)
        tanggal = pd.to_datetime(tanggal, dayfirst=True)
        data = df[df['tanggal'] == tanggal]
        
        if data.empty:
            return {'error': 'Tanggal tidak ditemukan dalam data kalender Jawa.'}
        
        row = data.iloc[0]
        return {
            'tanggal': tanggal.strftime("%A, %d %B %Y"),
            'hari': row['hari'],
            'pasaran': row['pasaran'],
            'neptu': int(row['neptu'])
        }
    except Exception as e:
        return {'error': f'Gagal membaca data kalender: {str(e)}'}
