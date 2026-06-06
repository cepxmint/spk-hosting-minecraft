# Legenda TOPSIS

## Step 1 - Matriks Keputusan

| Simbol | Arti | Contoh |
|--------|------|--------|
| X_Harga | Nilai asli harga dari data mentah | $10.00 |
| X_RAM | Nilai asli RAM dari data mentah | 4 GB |
| X_Storage | Nilai asli storage dari data mentah | 40 GB |
| X_Slot | Nilai asli slot pemain dari data mentah | 80 |
| X_Uptime | Nilai asli uptime dari data mentah | 99.9% |
| X_vCPU | Nilai asli vCPU dari data mentah | 2 |

## Step 2 - Normalisasi

| Simbol | Arti | Cara Dapet |
|--------|------|------------|
| penyebut_Harga | Angka pembagi buat kolom Harga | Semua X_Harga dikuadratkan, dijumlah, diakar |
| R_Harga | Harga setelah dinormalisasi | X_Harga dibagi penyebut_Harga |

Lakukan hal yang sama untuk RAM, Storage, Slot, Uptime, vCPU.

## Step 3 - Normalisasi Terbobot

| Simbol | Arti | Cara Dapet |
|--------|------|------------|
| Bobot_Harga | Tingkat kepentingan Harga | Ditentukan user: 0.20 |
| Y_Harga | Harga setelah dikali bobot | R_Harga dikali Bobot_Harga |

Lakukan hal yang sama untuk RAM, Storage, Slot, Uptime, vCPU.

## Step 4 - Solusi Ideal

| Simbol | Arti | Cara Dapet |
|--------|------|------------|
| A+ | Hosting impian (nilai terbaik tiap kolom) | Untuk benefit ambil Y terbesar, untuk cost ambil Y terkecil |
| A- | Hosting terburuk (nilai terjelek tiap kolom) | Untuk benefit ambil Y terkecil, untuk cost ambil Y terbesar |

## Step 5 - Jarak Euclidean

| Simbol | Arti | Cara Dapet |
|--------|------|------------|
| D+ | Jarak hosting ke A+ (ke hosting impian) | Makin kecil makin bagus |
| D- | Jarak hosting ke A- (dari hosting terburuk) | Makin besar makin bagus |

## Step 6 - Nilai Preferensi

| Simbol | Arti | Cara Dapet |
|--------|------|------------|
| V | Skor akhir tiap hosting (0-1) | D- dibagi (D+ ditambah D-) |

Makin mendekati 1, makin bagus.

## Step 7 - Ranking

| Simbol | Arti | Cara Dapet |
|--------|------|------------|
| Rank | Peringkat hosting | Diurutkan dari V terbesar ke terkecil |

## Ringkasan Operator

| Operator | Maksud |
|----------|--------|
| + | Ditambah |
| - | Dikurang |
| x atau * | Dikali |
| ÷ atau / | Dibagi |
| ^2 atau kuadrat | Dikali angka itu sendiri |
| akar() | Kebalikan dari kuadrat |
| jumlah() | Semua ditambah |
