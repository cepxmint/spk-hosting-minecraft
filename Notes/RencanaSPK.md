# 📋 Rencana SPK — Tugas Akhir

## Study Case
**Rekomendasi Platform Hosting Server Minecraft**
Membantu pemain memilih hosting server Minecraft terbaik berdasarkan kriteria-kriteria tertentu.

## Metode
- **TOPSIS** (dari Materi/SPK_Pertemuan5_TOPSIS_dan_ELECTRE.txt) — metode utama untuk ranking
- Mungkin tambahan: **AHP** untuk bobot kriteria, atau **BORDA** kalo pake banyak DM

## Dataset
- Setiap tier/plan hosting = 1 baris data
- Target: **50+ baris**
- Target: **5+ kriteria per baris**
- Sumber data: website resmi masing-masing hosting

## Kriteria (sementara)
1. Harga per bulan (Rp / USD)
2. RAM (GB)
3. Storage (GB)
4. Jumlah slot pemain
5. Uptime (%)
6. CPU / performa

## Platform Hosting + Tier (sementara)
### Free Hosting
1. Aternos Free
2. Minefort Free
3. Server.pro Free
4. FalixNodes Free
5. ScalaCube Free

### Paid Hosting
6. Aternos Premium (~€2.99)
7. Minefort Paid (~$5)
8. Server.pro Premium+ (~$6)
9. Server.pro Extreme (~$12)
10. Shockbyte Dirt ($2.50/1GB)
11. Shockbyte Stone ($5/2GB)
12. Shockbyte Iron ($10/4GB)
13. Shockbyte Gold ($20/8GB)
14. Shockbyte Titan ($40/16GB)
15. BisectHosting Budget ($2.99/2GB)
16. BisectHosting Premium 4GB ($9.99)
17. BisectHosting Premium 8GB ($18.99)
18. BisectHosting Premium 16GB ($35.99)
19. PebbleHost Basic ($3/2GB)
20. PebbleHost Standard ($6/4GB)
21. PebbleHost Pro ($12/8GB)
22. PebbleHost Elite ($24/16GB)
23. ScalaCube Entry ($2.50/1GB)
24. ScalaCube Small ($4.99/2GB)
25. ScalaCube Medium ($19.99/8GB)
26. ScalaCube Large ($39.99/16GB)
27. ScalaCube XL ($79.99/32GB)
28. Apex Hosting Basic ($7.49/2GB)
29. Apex Hosting Standard ($14.99/4GB)
30. Apex Hosting Pro ($29.99/8GB)
31. Apex Hosting Elite ($59.99/16GB)
32. MCProHosting Dirt ($7.99/2GB)
33. MCProHosting Stone ($15.99/4GB)
34. MCProHosting Iron ($29.99/8GB)
35. MCProHosting Gold ($59.99/16GB)
36. Sparked Host Basic ($1/2GB)
37. Sparked Host Standard ($6/4GB)
38. Sparked Host Pro ($12/8GB)
39. Sparked Host Elite ($24/16GB)
40. Hostinger Starter ($8.99/2GB)
41. Hostinger Professional ($12.99/4GB)
42. Hostinger Enterprise ($19.99/8GB)
43. Nodecraft ($9.98/2GB)
44. GGServers ($3/mo entry)
45. Akliz ($4.50/mo entry)
46. Godlike.host ($6.39/2GB)
47. Host Havoc
48. ServerMiner ($5/mo)
49. G-Portal ($4.85/mo)
50. exaroton (pay-as-you-go)
51. Pine Hosting
52. CloudNord
53. Nitrado
54. GTX Gaming
55. DatHost
56. Bloom.host
57. WiseHosting
58. Vultr (DIY VPS)
59. Low.MS
60. BlueFang Solutions
61. Streamline Servers

**Catatan:** Masih perlu dicek tiap tier (RAM, harga, storage, slot, uptime) dari websitenya masing-masing. Ini baru daftar platform, nanti diisi detailnya pas bikin dataset.

## Output Files
| File | Lokasi | Status |
|------|--------|--------|
| Dataset Excel | `Excel/Dataset_Hosting_Minecraft.xlsx` | ✅ 73 baris, 22 platform |
| Dataset CSV | `Dataset/Dataset_Hosting_Minecraft.csv` | ✅ |
| Laporan TOPSIS | `Excel/Hasil_TOPSIS_Hosting_Minecraft.docx` | ✅ |
| Script dataset | `Python/generate_dataset_real.py` | ✅ |
| Script TOPSIS+DOCX | `Python/topsis_docx.py` | ✅ |
| Script dummy | `Python/generate_dataset.py` | ✅ (old) |

## Tools / Library
- Python: `openpyxl` ✅, `pandas` ✅, `selenium` ✅, `beautifulsoup4` ✅, `python-docx` ✅
- Metode utama: **TOPSIS**
- Bobot: Harga=0.20, RAM=0.20, Storage=0.10, Slot=0.10, Uptime=0.25, vCPU=0.15

## Hasil TOPSIS (Top 5)
1. **Hostinger - Panel8** (V=0.810) — 32GB, 400GB, $27.99
2. Godlike.host - Elite (V=0.614) — 32GB, 320GB, $64.99
3. Hostinger - Panel4 (V=0.593) — 16GB, 200GB, $13.99
4. Sparked Host - Elite (V=0.544) — 16GB, 160GB, $24.00
5. PebbleHost - Elite (V=0.544) — 16GB, 160GB, $24.00

## Validasi Data
- ✅ Sumber data: `Notes/SumberData.md`
- ✅ 13 platform diverifikasi langsung dari website resmi
- ✅ 9 platform dari artikel pihak ketiga (link tercantum)
- ✅ Nilai "Unlimited" diganti dengan angka realistis (storage: RAM×10, slot: RAM×20)
- ⚠️ Data free hosting (uptime) dari estimasi komunitas
- ❌ **Aternos Premium dihapus** — Aternos murni gratis

## Status
- ✅ Dataset final selesai (72 baris, 22 platform, 8 kolom)
- ✅ Validasi data + sumber tercatat
- ✅ Script perhitungan TOPSIS + DOCX
- ✅ Bobot kriteria sudah divalidasi oleh user (Harga=0.20, RAM=0.20, Storage=0.10, Slot=0.10, Uptime=0.25, vCPU=0.15)
- ✅ **SELESAI** 🎉

## Progress Notes
- 30 Mei 2026: Ide disetujui, pendekatan per-tier dipilih
- 30 Mei 2026: Dataset real + TOPSIS + DOCX selesai dibuat
- 30 Mei 2026: Validasi data — 3 error ditemukan & diperbaiki
