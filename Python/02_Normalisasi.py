import pandas as pd
import numpy as np

print("=" * 60)
print("STEP 2 - NORMALISASI MATRIKS")
print("=" * 60)

df = pd.read_csv("Dokumen/Dataset_Hosting_Minecraft.csv")
kriteria = ["Harga (USD/mo)", "RAM (GB)", "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"]

X = df[kriteria].values.astype(float)

print()
print("Tiap kolom di kuadratkan, lalu semua dijumlah, lalu diakarkan:")
print()

penyebut_list = []
for j, k in enumerate(kriteria):
    kuadrat = X[:, j] ** 2
    jumlah = kuadrat.sum()
    penyebut = np.sqrt(jumlah)
    penyebut_list.append(penyebut)
    print(f"  Kolom {k}:")
    print(f"    Semua {len(X)} angka dikuadratkan, hasilnya dijumlah = {jumlah:.4f}")
    print(f"    Lalu diakar -> penyebut = {penyebut:.6f}")
    print()

penyebut = np.array(penyebut_list)
R = X / penyebut

print("=" * 60)
print("HASIL NORMALISASI (R)")
print("5 baris pertama:")
print("=" * 60)
print()

df_out = df[["Platform", "Tier"]].copy()
for j, k in enumerate(kriteria):
    df_out[k] = R[:, j]

print(df_out.head(5).to_string(index=False))
print()
print(f"  ... dan {len(df_out) - 5} baris lainnya")
print()
print("=" * 60)
print("Output -> CSV/02_Normalisasi.csv")
print("=" * 60)

df_out.to_csv("CSV/02_Normalisasi.csv", index=False)
