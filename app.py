
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Dasbor Visualisasi Data Gratis")
st.write("Aplikasi ini dibuat gratis tanpa resource komputer lokal!")

# Membuat data tiruan
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Pendapatan', 'Pengeluaran', 'Keuntungan']
)

# Membuat grafik interaktif dengan Plotly
fig = px.line(chart_data, title="Tren Keuangan Perusahaan")
st.plotly_chart(fig)
