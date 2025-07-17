import streamlit as st
import pandas as pd
from utils import lookup_kalender

st.set_page_config(
    page_title="🧙 Primbon Jawa Lengkap",
    page_icon="🧙",
    layout="centered",
)

st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: brown;'>🧙‍ Primbon Jawa Lengkap</h1>
        <p style='font-size: 18px;'>Menyingkap rahasia weton, neptu, watak dan jodoh berdasarkan perhitungan Jawa kuno</p>
        <hr style='border: 2px solid brown;'>
    </div>
""", unsafe_allow_html=True)

nama = st.text_input("Nama lengkap")
tanggal_lahir = st.text_input("Tanggal lahir (dd/mm/yyyy)", placeholder="Contoh: 22/12/1979")

if nama and tanggal_lahir:
    try:
        hasil = lookup_kalender(tanggal_lahir)
        st.success(f"Halo {nama}! Kamu lahir pada hari **{hasil['hari']} {hasil['pasaran']}**")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Hari", hasil['hari'])
        with col2:
            st.metric("Pasaran", hasil['pasaran'])

        st.markdown("""
            <div style='text-align: center; font-size: 20px; margin-top: 20px;'>
                🔹 Jumlah Neptu: <b style='color: green;'>%d</b>
            </div>
