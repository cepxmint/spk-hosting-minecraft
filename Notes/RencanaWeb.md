# Rencana Web - SPK Hosting Minecraft

## Tech Stack
- HTML + CSS + JavaScript (pure, no framework)
- Font: Figtree (Google Fonts)
- Math rendering: MathJax CDN
- Hosting: static (GitHub Pages / Netlify / Vercel)

## Warna
- Background: `#f2f2f2`
- Teks utama: `#222222`
- Putih: `#ffffff`
- Aksen biru: `#1a56db` (dari PPT)

## Halaman

| Halaman | File | Isi |
|---------|------|-----|
| 1 | `index.html` | Beranda - intro studi kasus, statistik (22 platform, 72 alternatif, 6 kriteria), navigasi ke halaman lain |
| 2 | `dataset.html` | Tabel daftar 72 hosting, bisa search & sort, tiap baris ada tombol "Kunjungi" menuju website resmi platform |
| 3 | `metode.html` | Step-by-step TOPSIS - 7 langkah lengkap dari `topsis_docx.py`: matriks keputusan, normalisasi, bobot, solusi ideal, jarak, preferensi, ranking. Tiap langkah: rumus (MathJax) + tabel hasil + penjelasan. Ada simulasi perhitungan interaktif. |
| 4 | `hasil.html` | Ranking top 10 (highlight juara), tabel ranking 72 lengkap, analisis kenapa Hostinger unggul |
| 5 | `kesimpulan.html` | Kesimpulan & rekomendasi |

## Struktur Folder
```
spk-hosting-minecraft/
├── index.html
├── dataset.html
├── metode.html
├── hasil.html
├── kesimpulan.html
├── css/
│   └── style.css
├── js/
│   ├── data.js          ← data 72 hosting (array of objects)
│   ├── topsis.js        ← engine TOPSIS (normalisasi, bobot, jarak, preferensi)
│   └── main.js          ← navigasi, utility, interaktivitas
└── README.md (optional)
```

## Fitur
- [x] Responsif (mobile-friendly)
- [x] Search & sort tabel dataset
- [x] Tombol "Kunjungi" per platform (link ke website resmi)
- [x] Render rumus LaTeX (MathJax)
- [x] Simulasi perhitungan TOPSIS interaktif
- [x] Navigasi antar halaman

## Sumber Data
- Dataset: `Dokumen/Dataset_Hosting_Minecraft.csv` (72 baris, 22 platform)
- Sumber: `Notes/SumberData.md`
- Perhitungan: `Python/topsis_docx.py`, `Python/generate_ppt.py`
