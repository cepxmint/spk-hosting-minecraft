import pandas as pd

print("=" * 60)
print("STEP 7 - RANKING")
print("=" * 60)

df = pd.read_csv("CSV/06_NilaiPreferensi.csv")

df_rank = df.sort_values("V", ascending=False).reset_index(drop=True)
df_rank.index = df_rank.index + 1
df_rank.index.name = "Rank"

print()
print("TOP 10 Hosting Terbaik:")
print("=" * 60)
print()
print(df_rank.head(10).to_string(index=True, index_names=True))
print()

print("=" * 60)
print("Output -> CSV/07_Ranking.csv")
print("=" * 60)

df_rank.to_csv("CSV/07_Ranking.csv", index=True, index_label="Rank")
