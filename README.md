<div align="center">

# 🔢 Newton Method Application

### Aplikasi interaktif untuk menghitung akar persamaan menggunakan Metode Newton

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-rzikydn-181717?style=for-the-badge&logo=github)](https://github.com/rzikydn)

</div>

---

## ✨ Fitur Utama

<table>
<tr>
<td width="50%">

### 🎲 Random Mode
- ✅ Generate fungsi polynomial otomatis (derajat 2-3)
- ✅ Hitung akar persamaan otomatis
- ✅ Visualisasi grafik fungsi dan konvergensi

</td>
<td width="50%">

### ✍️ Manual Input Mode
- ✅ Input fungsi dan turunannya secara manual
- ✅ Atur parameter perhitungan lengkap
- ✅ Kustomisasi range plot
- ✅ Detail proses per iterasi

</td>
</tr>
</table>

### 📊 Visualisasi & Export
- 📈 Grafik fungsi dengan titik iterasi
- 📉 Grafik konvergensi error (log scale)
- 📋 Tabel iterasi lengkap dengan semua nilai
- 💾 Export hasil ke CSV

---

## 🚀 Quick Start

### 📦 Requirements

```bash
Python 3.7+  |  Streamlit  |  NumPy  |  Pandas  |  Matplotlib
```

### ⚡ Instalasi Cepat

```bash
# Clone repository
git clone https://github.com/rzikydn/NewtonMethod.git
cd NewtonMethod

# Install dependencies
pip install -r requirements.txt
```

### 🎯 Menjalankan Aplikasi

```bash
streamlit run newton_method_app.py
```

Kemudian buka browser di: **http://localhost:8501**

---

## 📖 Cara Penggunaan

### 🎲 Random Mode
1. 🎲 Klik tombol **"Generate Random Function"**
2. 🔄 Fungsi polynomial di-generate otomatis
3. ⚙️ Atur parameter (Tebakan Awal, Toleransi, Max Iterasi)
4. 🚀 Klik **"Hitung dengan Newton Method"**
5. 📊 Lihat hasil, tabel iterasi, dan visualisasi

### ✍️ Manual Input Mode
1. ✏️ Masukkan fungsi `f(x)` dan turunannya `f'(x)`
   > Contoh: `x**3 - x - 2` dan `3*x**2 - 1`
2. ⚙️ Atur parameter perhitungan
3. 📐 Atur range plot (min dan max)
4. 🚀 Klik **"Hitung dengan Newton Method"**
5. 📊 Lihat hasil dan analisis detail

---

## 📝 Format Penulisan Fungsi

| Elemen | Format | Contoh |
|--------|--------|---------|
| Variabel | `x` | `x` |
| Pangkat | `x**n` | `x**2`, `x**3` |
| Perkalian | `n*x` | `2*x`, `3*x**2` |
| Penjumlahan | `+` | `x**2 + 3*x + 2` |
| Pengurangan | `-` | `x**3 - x - 2` |

### ✅ Contoh Fungsi Valid:
```python
x**3 - x - 2          # Kubik
x**2 + 3*x + 2        # Kuadrat
x**4 - 2*x**2 + 1     # Pangkat 4
```

---

## 🧮 Metode Newton

<div align="center">

### Formula Dasar

```math
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)
```

</div>

### 🔄 Algoritma

```
1️⃣ Mulai dengan tebakan awal x₀
2️⃣ Hitung f(x₀) dan f'(x₀)
3️⃣ Hitung x₁ = x₀ - f(x₀)/f'(x₀)
4️⃣ Ulangi hingga konvergen atau max iterasi
```

### ⏹️ Kondisi Berhenti
- ✅ `|xₙ₊₁ - xₙ| < toleransi`
- ✅ Iterasi maksimum tercapai

---

## 📁 Struktur File

```
NewtonMethod/
│
├── 📄 newton_method_app.py    # Aplikasi utama
├── 📖 README.md                # Dokumentasi
└── 📋 requirements.txt         # Dependencies
```

---

## 🛠️ Teknologi

<div align="center">

| Teknologi | Fungsi |
|-----------|--------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Web Framework |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Komputasi Numerik |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Data Processing |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) | Visualisasi |

</div>

---

## 🎨 Fitur Tambahan

- 🌙 Dark mode support
- 📱 Responsive design
- 💾 Export ke CSV
- 🔍 Detail proses per iterasi
- ⚠️ Error handling

---

## 👨‍💻 Author

<div align="center">

**Tugas Metode Numerik - Operations Research**

[![GitHub](https://img.shields.io/badge/GitHub-rzikydn-181717?style=for-the-badge&logo=github)](https://github.com/rzikydn)

</div>

---

## 📄 License

MIT License - feel free to use this project for learning purposes!

---

<div align="center">

### Dibuat dengan ❤️ menggunakan Streamlit

⭐ **Star this repo if you find it helpful!** ⭐

</div>
