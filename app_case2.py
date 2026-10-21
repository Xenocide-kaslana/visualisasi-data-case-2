import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Mahasiswa", page_icon="🎓", layout="wide")
st.title("🎓 Dashboard Bedah Kasus 2 - Raffi Kurniawan (241041001)")
st.markdown("Analisis Profil Mahasiswa menggunakan 1000 data sintesis.")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('dataset_mahasiswa_1000.csv')

df = load_data()

# Metrik Utama
col1, col2, col3 = st.columns(3)
col1.metric("Total Mahasiswa", f"{len(df)} Orang")
col2.metric("Rata-rata IPK", f"{df['IPK'].mean():.2f}")
col3.metric("Rata-rata Usia", f"{df['Usia'].mean():.1f} Tahun")
st.divider()

# GRAFIK BARIS 1
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Distribusi Mahasiswa per Semester")
    st.caption("Kategorik Ordinal: Bar Chart Berurutan")
    # Menghitung jumlah per semester lalu diurutkan (1 -> 2 -> 3 dst)
    sem_count = df['Semester'].value_counts().reset_index()
    sem_count.columns = ['Semester', 'Jumlah']
    sem_count = sem_count.sort_values('Semester')
    
    # Bikin jadi string biar Plotly paham ini kategori berurutan, bukan angka biasa
    sem_count['Semester'] = sem_count['Semester'].astype(str) 
    
    fig_bar = px.bar(sem_count, x='Semester', y='Jumlah', text_auto=True, color='Semester')
    st.plotly_chart(fig_bar, use_container_width=True)

with col_b:
    st.subheader("Sebaran IPK per Jurusan (Melihat Outlier)")
    st.caption("Numerik Kontinu: Box Plot")
    # Box plot untuk melihat sebaran, rata-rata, dan outlier data nilai IPK
    fig_box = px.box(df, x='Jurusan', y='IPK', color='Jurusan', points="outliers")
    st.plotly_chart(fig_box, use_container_width=True)

# GRAFIK BARIS 2
col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Distribusi Usia Mahasiswa")
    st.caption("Numerik Kontinu: Histogram")
    fig_hist = px.histogram(df, x='Usia', nbins=10, color_discrete_sequence=['indianred'])
    st.plotly_chart(fig_hist, use_container_width=True)

with col_d:
    st.subheader("Proporsi Mahasiswa per Jurusan")
    st.caption("Kategorik Nominal: Pie Chart")
    jur_count = df['Jurusan'].value_counts().reset_index()
    jur_count.columns = ['Jurusan', 'Jumlah']
    fig_pie = px.pie(jur_count, values='Jumlah', names='Jurusan', hole=0.3)
    st.plotly_chart(fig_pie, use_container_width=True)

# TABEL DATA
st.subheader("Tabel Dataset Mentah")
st.dataframe(df, use_container_width=True)