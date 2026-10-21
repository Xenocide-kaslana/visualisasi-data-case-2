import pandas as pd
import numpy as np
import random

# Kunci seed biar data acaknya tetap sama tiap dijalankan
np.random.seed(42)
random.seed(42)

# Mengembangkan Jurusan dari 2 sampel awal (Sistem Informasi, Manajemen)
jurusans = ['Sistem Informasi', 'Manajemen', 'Teknik Informatika', 'Akuntansi', 'Ilmu Komunikasi']

data = []

# Generate 1000 baris data
for _ in range(1000):
    jurusan = random.choice(jurusans)
    
    # Semester (1 sampai 8) - Kategorik Ordinal
    semester = random.randint(1, 8)
    
    # IPK - Numerik Kontinu (Rata-rata mahasiswa IPK nya 3.2, direntang 2.0 sampai 4.0)
    # Dibulatkan 2 desimal seperti di referensi gambar (contoh: 3.85)
    ipk = round(np.clip(np.random.normal(3.2, 0.4), 2.0, 4.0), 2)
    
    # Usia - Numerik (Terkorelasi dengan semester agar masuk akal. Maba = ~18/19 thn)
    usia = 18 + (semester // 2) + random.randint(0, 1)
    
    data.append([jurusan, semester, ipk, usia])

# Jadikan DataFrame
df = pd.DataFrame(data, columns=['Jurusan', 'Semester', 'IPK', 'Usia'])

# Proses Analisis Dasar dengan Python
print("=== ANALISIS DATA PROFIL MAHASISWA ===")
print("Rata-rata IPK Keseluruhan:", round(df['IPK'].mean(), 2))
print("Rata-rata Usia Keseluruhan:", round(df['Usia'].mean(), 1))
print("\nRata-rata IPK per Jurusan:")
print(df.groupby('Jurusan')['IPK'].mean().round(2).sort_values(ascending=False))

# Simpan jadi CSV
df.to_csv('dataset_mahasiswa_1000.csv', index=False)
print("\n[SUCCESS] 1000 Data Mahasiswa berhasil dibuat: dataset_mahasiswa_1000.csv")