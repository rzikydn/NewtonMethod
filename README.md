# Newton Method Application

Aplikasi interaktif berbasis **Streamlit** untuk menghitung akar persamaan menggunakan **Metode Newton** (Newton-Raphson Method).

## Fitur Utama

### 1. Random Mode
- Generate fungsi polynomial secara otomatis (derajat 2 atau 3)
- Hitung akar persamaan secara otomatis
- Visualisasi grafik fungsi dan konvergensi

### 2. Manual Input Mode
- Input fungsi dan turunannya secara manual
- Atur parameter perhitungan (tebakan awal, toleransi, max iterasi)
- Atur range plot untuk visualisasi
- Lihat detail proses per iterasi

### 3. Visualisasi
- Grafik fungsi dengan titik iterasi
- Grafik konvergensi error (log scale)
- Tabel iterasi lengkap

### 4. Export Data
- Download hasil perhitungan dalam format CSV

## Screenshot

### Random Mode
Generate fungsi polynomial secara random dan hitung akarnya otomatis.

### Manual Input Mode
Input fungsi sendiri dan atur semua parameter perhitungan.

## Instalasi

### Requirements
- Python 3.7+
- Streamlit
- NumPy
- Pandas
- Matplotlib

### Install Dependencies

```bash
pip install streamlit numpy pandas matplotlib
```

## Cara Menjalankan

1. Clone repository ini:
```bash
git clone https://github.com/rzikydn/NewtonMethod.git
cd NewtonMethod
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
streamlit run newton_method_app.py
```

4. Buka browser dan akses:
```
http://localhost:8501
```

## Penggunaan

### Random Mode
1. Klik tombol "Generate Random Function"
2. Fungsi polynomial akan di-generate secara otomatis
3. Atur parameter (Tebakan Awal, Toleransi, Max Iterasi)
4. Klik "Hitung dengan Newton Method"
5. Lihat hasil perhitungan, tabel iterasi, dan visualisasi

### Manual Input Mode
1. Masukkan fungsi f(x) dan turunannya f'(x)
   - Contoh: `x**3 - x - 2` dan `3*x**2 - 1`
2. Atur parameter perhitungan
3. Atur range plot (min dan max)
4. Klik "Hitung dengan Newton Method"
5. Lihat hasil dan analisis detail

## Format Penulisan Fungsi

- Gunakan `x` sebagai variabel
- Pangkat: `x**2`, `x**3`, `x**4`
- Perkalian: `2*x`, `3*x**2`
- Contoh fungsi valid:
  - `x**3 - x - 2`
  - `x**2 + 3*x + 2`
  - `x**4 - 2*x**2 + 1`

## Metode Newton

### Formula
```
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)
```

### Kondisi Berhenti
- `|xₙ₊₁ - xₙ| < toleransi`
- Iterasi maksimum tercapai

### Cara Kerja
1. Mulai dengan tebakan awal x₀
2. Hitung nilai fungsi f(x₀) dan turunannya f'(x₀)
3. Hitung tebakan berikutnya: x₁ = x₀ - f(x₀)/f'(x₀)
4. Ulangi hingga konvergen atau mencapai iterasi maksimum

## Struktur File

```
NewtonMethod/
│
├── newton_method_app.py    # Aplikasi utama
├── README.md                # Dokumentasi
└── requirements.txt         # Dependencies
```

## Teknologi yang Digunakan

- **Streamlit**: Framework web app untuk Python
- **NumPy**: Komputasi numerik
- **Pandas**: Manipulasi data dan tabel
- **Matplotlib**: Visualisasi grafik

## Fitur Tambahan

- Dark mode support (via Streamlit theme)
- Responsive design
- Export hasil ke CSV
- Detail proses per iterasi
- Error handling

## Kontribusi

Tugas Metode Numerik - Operations Research

## Lisensi

MIT License

## Kontak

GitHub: [@rzikydn](https://github.com/rzikydn)

---

Dibuat dengan ❤️ menggunakan Streamlit
