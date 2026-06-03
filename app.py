
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Konfigurasi Halaman Dashboard
st.set_page_config(page_title="Dasbor Gini Rasio Indonesia", layout="wide")
st.title("📊 Peta Tren Gini Rasio Provinsi di Indonesia (1980 - Sekarang)")
st.write("Visualisasi tingkat ketimpangan pengeluaran di Indonesia menggunakan Streamlit dan Plotly.")

# 2. Membuat Data Simulasi Histori Gini Rasio Provinsi
# Catatan: Data asli historis berkala per provinsi dapat diunduh di Badan Pusat Statistik (BPS)
provinsi_list = [
    {"nama": "ACEH", "lat": 4.1755, "lon": 96.8103},
    {"nama": "SUMATERA UTARA", "lat": 2.1121, "lon": 99.1348},
    {"nama": "SUMATERA BARAT", "lat": -0.7399, "lon": 100.8000},
    {"nama": "RIAU", "lat": 0.5071, "lon": 101.5408},
    {"nama": "DKI JAKARTA", "lat": -6.2088, "lon": 106.8456},
    {"nama": "JAWA BARAT", "lat": -7.0909, "lon": 107.6689},
    {"nama": "JAWA TENGAH", "lat": -7.1510, "lon": 110.1403},
    {"nama": "DI YOGYAKARTA", "lat": -7.8753, "lon": 110.4262},
    {"nama": "JAWA TIMUR", "lat": -7.5361, "lon": 112.2384},
    {"nama": "BALI", "lat": -8.4095, "lon": 115.1889},
    {"nama": "SULAWESI SELATAN", "lat": -3.6687, "lon": 119.9740},
    {"nama": "PAPUA", "lat": -4.2699, "lon": 138.0803}
]

tahun_list = list(range(1980, 2027)) # Dari 1980 hingga data tahun terbaru 2026

data_rows = []
np.random.seed(42) # Mengunci pola acak agar simulasi data logis sesuai tren BPS

for prov in provinsi_list:
    # Membuat tren dasar: Rasio Gini Indonesia umumnya naik dari 1980an dan mulai melandai/turun di beberapa tahun terakhir
    base_gini = np.random.uniform(0.25, 0.32) 
    for index, tahun in enumerate(tahun_list):
        # Simulasi fluktuasi ekonomi makro (misal: naik jelang 2010an, melandai di 2025/2026)
        if tahun < 2000:
            growth = index * 0.002
        elif tahun < 2015:
            growth = (20 * 0.002) + ((tahun - 2000) * 0.004)
        else:
            growth = (20 * 0.002) + (15 * 0.004) - ((tahun - 2015) * 0.002)
            
        gini_value = clamp_val = max(0.1, min(0.6, base_gini + growth + np.random.uniform(-0.01, 0.01)))
        
        data_rows.append({
            "Provinsi": prov["nama"],
            "Latitude": prov["lat"],
            "Longitude": prov["lon"],
            "Tahun": tahun,
            "Gini Rasio": round(gini_value, 3)
        })

df = pd.DataFrame(data_rows)

# 3. Fitur Interaktif Panel Kontrol di Sidebar
st.sidebar.header("⚙️ Pengaturan Peta")
pilihan_tahun = st.sidebar.slider("Pilih Tahun Analisis:", min_value=1980, max_value=2026, value=2025)

# Filter data berdasarkan tahun yang dipilih user
df_filtered = df[df["Tahun"] == pilihan_tahun]

# 4. Pembuatan Visualisasi Peta Terintegrasi
st.subheader(f"📍 Distribusi Geografis Ketimpangan Tahun {pilihan_tahun}")

fig_map = px.scatter_mapbox(
    df_filtered,
    lat="Latitude",
    lon="Longitude",
    size="Gini Rasio",
    color="Gini Rasio",
    color_continuous_scale=px.colors.sequential.YlOrRd, # Gradasi kuning ke merah tua (makin merah makin timpang)
    size_max=30,
    zoom=4,
    center={"lat": -2.5489, "lon": 118.0149}, # Fokus koordinat tengah NKRI
    mapbox_style="open-street-map",
    hover_name="Provinsi",
    hover_data={"Gini Rasio": True, "Latitude": False, "Longitude": False}
)

fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=500)
st.plotly_chart(fig_map, use_container_width=True)

# 5. Informasi Tambahan Ringkasan Statistik Nasional (Opsional)
st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Rata-rata Gini Rasio Nasional", value=f"{df_filtered['Gini Rasio'].mean():.3f}")
with col2:
    prov_tertinggi = df_filtered.loc[df_filtered['Gini Rasio'].idxmax()]
    st.metric(label="Ketimpangan Tertinggi", value=f"{prov_tertinggi['Gini Rasio']}", delta=prov_tertinggi['Provinsi'], delta_color="inverse")
with col3:
    prov_terendah = df_filtered.loc[df_filtered['Gini Rasio'].idxmin()]
    st.metric(label="Ketimpangan Terendah", value=f"{prov_terendah['Gini Rasio']}", delta=prov_terendah['Provinsi'])
