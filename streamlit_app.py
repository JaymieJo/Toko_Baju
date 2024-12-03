import streamlit as st
import pandas as pd

# Judul halaman
st.title("Toko Baju Online")

# Deskripsi halaman
st.write("Selamat datang di toko baju online kami! Di sini Anda dapat menemukan berbagai macam baju dengan harga terjangkau.")

# Buat sidebar
with st.sidebar:
    # Kategori baju
    kategori = st.selectbox("Kategori", ["Semua", "Kaos", "Kemeja", "Celana", "Rok"])

    # Rentang harga
    harga_min, harga_max = st.slider("Rentang Harga", 0, 100, (0, 100))

    # Ukuran baju
    ukuran = st.multiselect("Ukuran", ["S", "M", "L", "XL", "XXL"])

    # Warna baju
    warna = st.multiselect("Warna", ["Merah", "Biru", "Hijau", "Kuning", "Hitam", "Putih"])

# Muat data baju
data = pd.read_png("th.png")

# Filter data baju
if kategori != "Semua":
    data = data[data["Kategori"] == kategori]
if harga_min > 0 or harga_max < 100:
    data = data[(data["Harga"] >= harga_min) & (data["Harga"] <= harga_max)]
if len(ukuran) > 0:
    data = data[data["Ukuran"].isin(ukuran)]
if len(warna) > 0:
    data = data[data["Warna"].isin(warna)]

# Tampilkan data baju
st.table(data)
