import pandas as pd

print("=" * 60)
print("STEP 4 - SOLUSI IDEAL")
print("=" * 60)

df = pd.read_csv("CSV/03_Terbobot.csv")
kriteria = ["Harga (USD/mo)", "RAM (GB)", "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"]

# Harga = cost (makin kecil makin bagus), sisanya benefit (makin besar makin bagus)
tipe = {
    "Harga (USD/mo)": "cost",
    "RAM (GB)": "benefit",
    "Storage (GB)": "benefit",
    "Slot Pemain": "benefit",
    "Uptime (%)": "benefit",
    "vCPU": "benefit"
}

data = df[kriteria].values.astype(float)

print()
print("Mencari A_Kriteria (A+) dan A-_Kriteria (A-):")
print(f"  Benefit -> A+ = MAX, A- = MIN")
print(f"  Cost    -> A+ = MIN, A- = MAX")
print()

hasil = []
for j, k in enumerate(kriteria):
    kolom = data[:, j]
    if tipe[k] == "benefit":
        a_plus = kolom.max()
        a_minus = kolom.min()
    else:
        a_plus = kolom.min()
        a_minus = kolom.max()
    hasil.append({"Kriteria": k, "Tipe": tipe[k], "A+": a_plus, "A-": a_minus})
    print(f"  {k} ({tipe[k]}):")
    print(f"    A+ = {a_plus:.6f}")
    print(f"    A- = {a_minus:.6f}")
    print()

print("=" * 60)
print("HASIL SOLUSI IDEAL")
print("=" * 60)
print()

df_hasil = pd.DataFrame(hasil)
print(df_hasil.to_string(index=False))
print()

print("=" * 60)
print("Output -> CSV/04_SolusiIdeal.csv")
print("=" * 60)

df_hasil.to_csv("CSV/04_SolusiIdeal.csv", index=False)
