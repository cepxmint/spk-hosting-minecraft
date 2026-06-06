# Dokumentasi Metodologi Pengerjaan — OpenCode

## 1. Ekstraksi Materi Perkuliahan (PDF ke Teks)

**Permasalahan:** Folder `Materi/` berisi file PDF materi perkuliahan Sistem Pendukung Keputusan yang perlu dianalisis untuk menentukan metode yang akan digunakan.

**Pendekatan:**
- Tool `Read` digunakan untuk membaca konten PDF secara langsung, dengan kemampuan merender dokumen PDF menjadi teks yang dapat dibaca oleh sistem.
- Untuk dokumen dengan jumlah halaman yang besar, parameter `offset` dan `limit` digunakan untuk membaca secara sekuensial per segmen halaman.
- Sebagai pendekatan alternatif, dikembangkan skrip `extract_pdf_txt.py` yang memanfaatkan library `pdfplumber` untuk mengekstraksi seluruh konten teks dari setiap file PDF di direktori `Materi/` dan menyimpannya ke format `.txt`.
- Berdasarkan hasil ekstraksi, ditemukan bahwa metode TOPSIS dan ELECTRE terdapat pada file `SPK_Pertemuan5_TOPSIS_dan_ELECTRE.txt`.
- Metode TOPSIS dipilih dengan alur perhitungan sebagai berikut: normalisasi matriks, normalisasi terbobot, penentuan solusi ideal positif dan negatif, perhitungan jarak Euclidean, perhitungan nilai preferensi, dan perankingan.

**Catatan Teknis:** Ekstraksi PDF tidak memerlukan pembukaan file secara manual — seluruh proses dilakukan melalui tool `Read` atau skrip ekstraksi massal.

---

## 2. Pengumpulan Dataset (WebSearch dan WebFetch)

**Permasalahan:** Diperlukan dataset riil dengan minimal 50 entri dan 5 kriteria mengenai platform hosting server Minecraft. Data tidak tersedia pada penyimpanan lokal.

**Pendekatan:**
- Tool `WebSearch` digunakan untuk melakukan pencarian informasi secara daring, khususnya daftar platform hosting Minecraft beserta spesifikasi harga dan konfigurasi sumber daya.
- Query pencarian yang digunakan antara lain: `minecraft server hosting price list 2026` dan `best minecraft hosting plans ram price`.
- Hasil pencarian mengarahkan pada laman resmi masing-masing penyedia hosting (Hostinger, Apex Hosting, Shockbyte, dan lain-lain) serta artikel perbandingan dari platform pihak ketiga.
- Tool `WebFetch` digunakan untuk mengambil konten dari setiap URL dan mengonversinya ke format markdown atau teks, sehingga data dapat diekstraksi secara terstruktur.

**Validasi Data:**
- Seluruh sumber data dicatat secara sistematis pada berkas `Notes/SumberData.md`.
- Setiap entri data diverifikasi melalui minimal dua sumber: laman resmi penyedia dan artikel perbandingan pihak ketiga.
- Proses validasi mengidentifikasi tiga anomali:
  1. Paket Aternos Premium tidak eksis (Aternos merupakan platform gratis murni)
  2. RAM Server.pro Free tercatat 1 GB, berdasarkan laman resmi seharusnya 2 GB
  3. MCProHosting telah bergabung (merger) dengan Apex Hosting sehingga data harga perlu disesuaikan
- Nilai placeholder "Unlimited" (999) yang berpotensi menimbulkan bias diganti dengan angka realistis berdasarkan pola proporsional (storage = RAM x 10, slot pemain = RAM x 20).

**Catatan Teknis:** Tool `WebSearch` dan `WebFetch` digunakan secara bergantian — pencarian untuk menemukan URL, kemudian pengambilan konten untuk mengekstraksi data. Untuk platform dengan laman berbasis JavaScript berat, artikel pihak ketiga yang telah merangkum spesifikasi digunakan sebagai sumber alternatif.

---

## 3. Pembuatan Berkas CSV

**Permasalahan:** Data yang terkumpul masih berbentuk teks tidak terstruktur dan perlu diorganisasikan ke dalam format tabel.

**Pendekatan:**
- Skrip `Python/generate_dataset_real.py` dikembangkan menggunakan library `pandas`.
- Data dimasukkan ke dalam struktur `list of dictionaries`, di mana setiap dictionary merepresentasikan satu entri (satu tier/plan hosting).
- Struktur kolom terdiri dari: Platform, Tier, Harga (USD/mo), RAM (GB), Storage (GB), Slot Pemain, Uptime (%), dan vCPU.
- Data diekspor ke format CSV melalui metode `pandas.DataFrame.to_csv()`.
- Berkas keluaran disimpan pada `Dataset/Dataset_Hosting_Minecraft.csv`.

**Catatan Teknis:** Penggunaan `pandas` dipilih karena kemudahan dalam manipulasi data tabular serta konversi ke berbagai format file.

---

## 4. Pembuatan Berkas Excel

**Permasalahan:** Diperlukan berkas dalam format Excel (.xlsx) untuk kompatibilitas dengan perangkat lunak perkantoran.

**Pendekatan:**
- Pada skrip yang sama (`generate_dataset_real.py`), ditambahkan ekspor ke format Excel menggunakan metode `pandas.DataFrame.to_excel()` dengan engine `openpyxl`.
- Satu baris kode: `df.to_excel("Excel/Dataset_Hosting_Minecraft.xlsx", index=False)`.
- Dengan demikian, satu skrip menghasilkan dua berkas keluaran secara simultan.

**Catatan Teknis:** Library `openpyxl` akan diinstalasi secara otomatis apabila belum tersedia pada lingkungan eksekusi.

---

## 5. Pembuatan Laporan Word dengan Notasi Matematika (LaTeX)

**Permasalahan:** Diperlukan laporan dalam format DOCX yang mencakup seluruh tahapan perhitungan TOPSIS, dilengkapi tabel perhitungan dan rumus matematika yang terformat dengan baik.

**Pendekatan:**
- Skrip `Python/topsis_docx.py` dikembangkan dengan alur sebagai berikut:
  1. Pembacaan dataset dari berkas CSV
  2. Perhitungan TOPSIS secara bertahap (normalisasi, normalisasi terbobot, solusi ideal, jarak Euclidean, preferensi, perankingan)
  3. Pembuatan dokumen Word menggunakan library `python-docx`

**Tabel Perhitungan:** Library `python-docx` digunakan dengan memanfaatkan API Table menggunakan gaya "Light Grid Accent 1". Terdapat tujuh tabel yang dihasilkan:
1. Data Awal (Matriks Keputusan)
2. Jenis Kriteria dan Bobot
3. Normalisasi Matriks
4. Normalisasi Terbobot
5. Solusi Ideal Positif dan Negatif
6. Jarak dan Nilai Preferensi
7. Hasil Ranking

**Rumus Matematika (LaTeX):**
- Pendekatan awal menggunakan OMML (Office Math Markup Language), yaitu format XML native untuk equation pada Microsoft Word. Namun, pendekatan ini gagal karena berkas tidak dapat dibuka oleh Microsoft Word.
- Pendekatan alternatif yang lebih stabil: **merender rumus LaTeX menjadi gambar PNG melalui matplotlib, kemudian menyematkan gambar tersebut ke dalam dokumen Word**.
- Fungsi `latex_to_image()` menggunakan library `matplotlib` dengan backend `Agg` (tanpa memerlukan graphical user interface).
- Engine mathtext bawaan matplotlib digunakan untuk memproses sintaks LaTeX, sehingga tidak memerlukan instalasi LaTeX secara terpisah.
- Gambar diproses dalam memori (BytesIO) tanpa menyimpan file sementara ke disk, kemudian ditambahkan ke dokumen melalui metode `add_picture()`.
- Tujuh rumus yang dirender: normalisasi, normalisasi terbobot, solusi ideal positif, solusi ideal negatif, jarak positif, jarak negatif, dan preferensi.

**Ilustrasi alur render rumus:**
```python
def latex_to_image(latex_str):
    fig, ax = plt.subplots(figsize=(6, 0.6))
    ax.axis("off")
    ax.text(0.5, 0.5, f"${latex_str}$", fontsize=14, ha="center", va="center")
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", transparent=True)
    return buf
```

**Catatan Teknis:** Pendekatan dengan matplotlib-image dipilih setelah dua percobaan konversi rumus yang menemui kegagalan — pertama dengan OMML langsung (gagal karena kompatibilitas), kedua melalui pipeline `latex2mathml` (terlalu kompleks). Pendekatan gambar memang menghasilkan ukuran berkas yang lebih besar (79 KB dibanding 46 KB), namun menjamin kompatibilitas lintas versi Microsoft Word.

---

## Rangkuman Alat dan Pustaka yang Digunakan

| Kebutuhan | Alat / Pustaka |
|-----------|----------------|
| Membaca materi PDF | Tool `Read`, library `pdfplumber` |
| Pencarian data | Tool `WebSearch`, `WebFetch` |
| Manipulasi data tabular | `pandas`, `numpy` |
| Ekspor CSV | `pandas.DataFrame.to_csv()` |
| Ekspor Excel | `pandas.DataFrame.to_excel()` + `openpyxl` |
| Pembuatan DOCX | `python-docx` |
| Rendering rumus LaTeX | `matplotlib` (mathtext engine) |
| Format dokumen | Heading, Table, Image, alignment (`python-docx`) |
| Validasi data | `WebFetch` cross-check manual |

## Alur Kerja Sistematis

1. **Eksplorasi** — Menggunakan tool `glob`, `grep`, dan `Read` untuk memahami struktur direktori dan konten berkas yang telah ada.
2. **Riset** — Menggunakan `WebSearch` untuk menemukan referensi data maupun solusi teknis.
3. **Ekstraksi detail** — Menggunakan `WebFetch` untuk mengambil konten dari URL spesifik.
4. **Implementasi** — Menggunakan `Write` untuk membuat skrip baru, `Edit` untuk memodifikasi skrip yang telah ada.
5. **Eksekusi dan pengujian** — Menggunakan `bash` untuk menjalankan skrip, menganalisis luaran, memperbaiki kesalahan, dan menjalankan ulang.
6. **Verifikasi** — Memeriksa luaran, memvalidasi data, dan memastikan berkas berfungsi sebagaimana mestinya.
7. **Dokumentasi** — Memperbarui berkas `Notes/RencanaSPK.md` dan `Notes/SumberData.md` secara berkala untuk mencatat perkembangan dan keputusan teknis.
