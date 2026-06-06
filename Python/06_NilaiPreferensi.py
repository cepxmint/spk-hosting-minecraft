import pandas as pd

print("=" * 60)
print("STEP 6 - NILAI PREFERENSI (V)")
print("=" * 60)

df = pd.read_csv("CSV/05_JarakEuclidean.csv")

print()
print(f"V = D- / (D+ + D-)")
print(f"  Kalo V deket 1 -> bagus")
print(f"  Kalo V deket 0 -> jelek")
print()

D_plus = df["D+"].values.astype(float)
D_minus = df["D-"].values.astype(float)

V = D_minus / (D_plus + D_minus)

df_out = df[["Platform", "Tier"]].copy()
df_out["V"] = V

print("=" * 60)
print("HASIL NILAI PREFERENSI")
print("5 baris pertama:")
print("=" * 60)
print()
print(df_out.head(5).to_string(index=False))
print()
print(f"  ... dan {len(df_out) - 5} baris lainnya")
print()

print("=" * 60)
print("Output -> CSV/06_NilaiPreferensi.csv")
print("=" * 60)

df_out.to_csv("CSV/06_NilaiPreferensi.csv", index=False)
