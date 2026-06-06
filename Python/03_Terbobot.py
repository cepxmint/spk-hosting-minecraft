import pandas as pd

print("=" * 60)
print("STEP 3 - NORMALISASI TERBOBOT")
print("=" * 60)

df = pd.read_csv("CSV/02_Normalisasi.csv")
kriteria = ["Harga (USD/mo)", "RAM (GB)", "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"]
bobot = [0.20, 0.20, 0.10, 0.10, 0.25, 0.15]

R = df[kriteria].values.astype(float)

print()
print(f"Bobot yang dipakai:")
for j, k in enumerate(kriteria):
    print(f"  {k} -> {bobot[j]}")
print()
print(f"Tiap nilai R dikali bobot masing-masing kriteria.")
print()

Y = R * bobot

print("=" * 60)
print("HASIL NORMALISASI TERBOBOT (Y)")
print("5 baris pertama:")
print("=" * 60)
print()

df_out = df[["Platform", "Tier"]].copy()
for j, k in enumerate(kriteria):
    df_out[k] = Y[:, j]

print(df_out.head(5).to_string(index=False))
print()
print(f"  ... dan {len(df_out) - 5} baris lainnya")
print()
print("=" * 60)
print("Output -> CSV/03_Terbobot.csv")
print("=" * 60)

df_out.to_csv("CSV/03_Terbobot.csv", index=False)
