import pandas as pd

df = pd.read_csv("Dokumen/Dataset_Hosting_Minecraft.csv")

print("=" * 60)
print("STEP 1 - MATRIKS KEPUTUSAN")
print("=" * 60)
print()
print("Data mentah 72 alternatif hosting dengan 6 kriteria.")
print()
print(f"Jumlah alternatif (baris) : {len(df)}")
print(f"Jumlah kriteria (kolom)   : {len(df.columns) - 2}")  # -2 karena Platform + Tier
print()
print("Kriteria yang dipakai:")
print("  1. Harga (USD/mo)   - cost   (makin murah makin baik)")
print("  2. RAM (GB)         - benefit (makin besar makin baik)")
print("  3. Storage (GB)     - benefit (makin besar makin baik)")
print("  4. Slot Pemain      - benefit (makin banyak makin baik)")
print("  5. Uptime (%)       - benefit (makin tinggi makin baik)")
print("  6. vCPU             - benefit (makin banyak makin baik)")
print()
print("5 baris pertama:")
print(df.head(5).to_string(index=False))
print()
print("=" * 60)
print("Output -> CSV/01_MatriksKeputusan.csv")
print("=" * 60)

df.to_csv("CSV/01_MatriksKeputusan.csv", index=False)
