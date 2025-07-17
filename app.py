import streamlit as st
from utils import hitung_weton

st.set_page_config(page_title="🧙 Primbon Jawa Lengkap", layout="centered")

st.title("🧙 Primbon Jawa Lengkap")
st.subheader("Pilih Menu")
st.markdown("---")

# Form input
with st.form("form_wetonan"):
    nama = st.text_input("Nama lengkap", "")
    tanggal_lahir = st.text_input("Tanggal lahir (dd/mm/yyyy)", "")
    submit = st.form_submit_button("Hitung Weton")

if submit:
    if not nama or not tanggal_lahir:
        st.warning("Silakan isi nama dan tanggal lahir terlebih dahulu.")
    else:
        hasil = hitung_weton(tanggal_lahir)

        if 'error' in hasil:
            st.error(hasil['error'])
        else:
            st.success(f"Hasil Wetonan untuk **{nama}**:")
            st.write(f"📅 Tanggal Lahir: {hasil['tanggal']}")
            st.write(f"🗓️ Hari Jawa: {hasil['hari']} {hasil['pasaran']}")
            st.write(f"🔢 Neptu: {hasil['neptu']}")
