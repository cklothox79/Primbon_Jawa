# app.py
import streamlit as st
from utils import hitung_weton

st.title("Primbon Jawa Lengkap")

nama = st.text_input("Masukkan nama lengkap:")
tanggal_lahir = st.date_input("Tanggal lahir:")

if st.button("Cek Weton"):
    weton_info = hitung_weton(tanggal_lahir)
    st.subheader(f"Weton: {weton_info['weton']}")
    st.write(f"Neptu: {weton_info['neptu']}")
    st.write(f"Sifat: {weton_info['sifat']}")
