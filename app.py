import streamlit as st
from utils import hitung_weton, cari_jodoh, tafsir_mimpi

st.set_page_config(page_title="Primbon Jawa", layout="centered")
st.title("🧙 Primbon Jawa Lengkap")

menu = st.selectbox("Pilih Menu", ["Wetonan", "Kecocokan Jodoh", "Tafsir Mimpi"])

if menu == "Wetonan":
    nama = st.text_input("Nama lengkap")
    tanggal_lahir = st.date_input("Tanggal lahir")
    if st.button("Hitung Weton"):
        hasil = hitung_weton(tanggal_lahir)
        st.success(f"Weton: {hasil['weton']}")
        st.info(f"Neptu: {hasil['neptu']} | Sifat: {hasil['sifat']}")

elif menu == "Kecocokan Jodoh":
    nama1 = st.text_input("Nama Anda")
    weton1 = st.text_input("Weton Anda (cth: Senin Kliwon)")
    nama2 = st.text_input("Nama Pasangan")
    weton2 = st.text_input("Weton Pasangan")
    if st.button("Cek Kecocokan"):
        hasil = cari_jodoh(weton1, weton2)
        st.success(f"Kecocokan: {hasil}")

elif menu == "Tafsir Mimpi":
    mimpi = st.text_input("Tuliskan mimpi Anda")
    if st.button("Tafsirkan"):
        hasil = tafsir_mimpi(mimpi)
        st.success(f"Arti mimpi: {hasil}")
