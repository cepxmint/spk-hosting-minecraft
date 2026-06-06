import pandas as pd
import numpy as np

print("=" * 60)
print("STEP 5 - JARAK EUCLIDEAN (D+ dan D-)")
print("=" * 60)

df_y = pd.read_csv("CSV/03_Terbobot.csv")
df_ideal = pd.read_csv("CSV/04_SolusiIdeal.csv")

kriteria = ["Harga (USD/mo)", "RAM (GB)", "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"]

Y = df_y[kriteria].values.astype(float)

A_plus = df_ideal[df_ideal["Tipe"] == "cost"]["A+"].values[0]
for _, row in df_ideal.iterrows():
    if row["Kriteria"] == "Harga (USD/mo)":
        A_plus_harga = row["A+"]
        A_minus_harga = row["A-"]
    elif row["Kriteria"] == "RAM (GB)":
        A_plus_ram = row["A+"]
        A_minus_ram = row["A-"]
    elif row["Kriteria"] == "Storage (GB)":
        A_plus_storage = row["A+"]
        A_minus_storage = row["A-"]
    elif row["Kriteria"] == "Slot Pemain":
        A_plus_slot = row["A+"]
        A_minus_slot = row["A-"]
    elif row["Kriteria"] == "Uptime (%)":
        A_plus_uptime = row["A+"]
        A_minus_uptime = row["A-"]
    elif row["Kriteria"] == "vCPU":
        A_plus_vcpu = row["A+"]
        A_minus_vcpu = row["A-"]

A_plus_arr = np.array([A_plus_harga, A_plus_ram, A_plus_storage, A_plus_slot, A_plus_uptime, A_plus_vcpu])
A_minus_arr = np.array([A_minus_harga, A_minus_ram, A_minus_storage, A_minus_slot, A_minus_uptime, A_minus_vcpu])

print(f"Mengitung jarak tiap hosting ke A+ dan A-")
print(f"  D+ = akar( jumlah( (Y - A+)^2 ) )")
print(f"  D- = akar( jumlah( (Y - A-)^2 ) )")
print()

D_plus_list = []
D_minus_list = []

for i in range(len(Y)):
    d_plus = np.sqrt(np.sum((Y[i] - A_plus_arr) ** 2))
    d_minus = np.sqrt(np.sum((Y[i] - A_minus_arr) ** 2))
    D_plus_list.append(d_plus)
    D_minus_list.append(d_minus)

df_out = df_y[["Platform", "Tier"]].copy()
df_out["D+"] = D_plus_list
df_out["D-"] = D_minus_list

print("=" * 60)
print("HASIL JARAK EUCLIDEAN")
print("5 baris pertama:")
print("=" * 60)
print()
print(df_out.head(5).to_string(index=False))
print()
print(f"  ... dan {len(df_out) - 5} baris lainnya")
print()

print("=" * 60)
print("Output -> CSV/05_JarakEuclidean.csv")
print("=" * 60)

df_out.to_csv("CSV/05_JarakEuclidean.csv", index=False)
