# Rencana Belajar TOPSIS

Belajar TOPSIS step-by-step pake Python + CSV.

## Struktur Folder
- `Python/` — tempat script Python (01-07) + dataset
- `CSV/` — tempat output CSV tiap step

## Alur 7 Step

### 01 MatriksKeputusan
Baca dataset, lihat isi tabel mentah.

### 02 Normalisasi
- Tiap kolom: kuadratkan semua nilai, jumlah, akar
- Bagi tiap nilai asli dengan hasil akar tadi
- Output: 02_Normalisasi.csv (R)

### 03 Terbobot
- Kalikan tiap nilai R dengan bobot masing-masing kriteria
- Output: 03_Terbobot.csv (Y)

### 04 SolusiIdeal
- Cari A+ (max benefit, min cost) dan A- (min benefit, max cost)
- Output: 04_SolusiIdeal.csv (A+, A-)

### 05 JarakEuclidean
- Hitung D+ dan D- tiap alternatif ke A+ dan A-
- Output: 05_JarakEuclidean.csv (D+, D-)

### 06 Preferensi
- V = D- / (D+ + D-)
- Output: 06_Preferensi.csv (V)

### 07 Ranking
- Urutkan dari V terbesar ke terkecil
- Output: 07_Ranking.csv

## Aturan Main
- Baca CSV dari step sebelumnya
- Print hasil antara biar keliatan prosesnya
- Output ke CSV/ folder
