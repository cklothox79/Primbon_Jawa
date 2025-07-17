import streamlit as st
from utils import lookup_kalender

st.set_page_config(page_title="🧙 Primbon Jawa Lengkap", layout="centered")

st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #f9f0e6; border-radius: 10px;'>
        <h1 style='color: brown;'>🧙 Primbon Jawa Lengkap</h1>
        <p style='font-size: 18px;'>Hitung Weton & Neptu berdasarkan kalender Jawa asli</p>
        <hr style='border: 2px solid brown;'>
    </div>
""", unsafe_allow_html=True)

st.subheader("🔢 Masukkan Data")

nama = st.text_input("Nama lengkap")
tanggal_lahir = st.text_input("Tanggal lahir (format: dd/mm/yyyy)")

if st.button("🔍 Hitung Weton"):
    try:
        hasil = lookup_kalender(tanggal_lahir)
        st.success(f"Hasil untuk {nama}:")
        st.info(f"""
        📅 Hari: **{hasil['hari']}**
        🌀 Pasaran: **{hasil['pasaran']}**
        🔢 Neptu: **{hasil['neptu']}**
        """)
        st.markdown("👉 Silakan buka menu lainnya di sidebar untuk melihat watak, jodoh, mimpi, dan hari baik.")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
