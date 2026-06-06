import pandas as pd

data = [
    # === FREE HOSTING ===
    ["Aternos", "Free", 0.00, 2,   5,  20, 85,  1],
    ["Minefort", "Free", 0.00, 2,   5,  20, 82,  1],
    ["Server.pro", "Free", 0.00, 2, 10,  10, 80,  1],
    ["FalixNodes", "Free", 0.00, 1,   5,   8, 78,  1],
    ["ScalaCube", "Free", 0.00, 1,   8,  10, 80,  1],

    # === PAID HOSTING ===
    # Minefort Paid
    ["Minefort", "Paid", 4.99, 4, 40, 40, 90, 2],

    # Server.pro
    ["Server.pro", "Premium+", 5.99,  3,  20,  20, 92,  2],
    ["Server.pro", "Extreme", 11.99,  6,  40,  40, 95,  3],

    # Shockbyte
    ["Shockbyte", "Dirt",   2.50,  1, 10,  20, 99.5, 1],
    ["Shockbyte", "Stone",  5.00,  2, 20,  40, 99.5, 1],
    ["Shockbyte", "Iron",  10.00,  4, 40,  80, 99.5, 2],
    ["Shockbyte", "Gold",  20.00,  8, 80, 160, 99.5, 2],
    ["Shockbyte", "Titan", 40.00, 16, 160, 320, 99.5, 4],

    # BisectHosting
    ["BisectHosting", "Budget",     2.99,  2,  20,  40, 99.9, 2],
    ["BisectHosting", "Premium4GB", 9.99,  4,  40,  80, 99.9, 2],
    ["BisectHosting", "Premium8GB", 18.99, 8,  80, 160, 99.9, 4],
    ["BisectHosting", "Premium16GB",35.99,16, 160, 320, 99.9, 4],

    # PebbleHost
    ["PebbleHost", "Basic",    3.00,  2,  20,  40, 99.7, 2],
    ["PebbleHost", "Standard", 6.00,  4,  40,  80, 99.7, 2],
    ["PebbleHost", "Pro",     12.00,  8,  80, 160, 99.7, 4],
    ["PebbleHost", "Elite",   24.00, 16, 160, 320, 99.7, 4],

    # ScalaCube
    ["ScalaCube", "Entry",  2.50,  1,  20,  20, 99.99, 1],
    ["ScalaCube", "Small",  4.99,  2,  40,  40, 99.99, 1],
    ["ScalaCube", "Medium", 19.99,  8,  80,  80, 99.99, 2],
    ["ScalaCube", "Large",  39.99, 16, 120, 120, 99.99, 4],
    ["ScalaCube", "XL",     79.99, 32, 200, 200, 99.99, 8],

    # Apex Hosting
    ["Apex Hosting", "Basic",    7.49,  2,  20,  40, 99.9, 2],
    ["Apex Hosting", "Standard",14.99,  4,  40,  80, 99.9, 2],
    ["Apex Hosting", "Pro",     29.99,  8,  80, 160, 99.9, 4],
    ["Apex Hosting", "Elite",   59.99, 16, 160, 320, 99.9, 4],

    # MCProHosting (merged with Apex, pricing updated)
    ["MCProHosting", "Dirt",  5.99,  2,  20,  40, 99.9, 2],
    ["MCProHosting", "Stone",11.99,  4,  40,  80, 99.9, 2],
    ["MCProHosting", "Iron", 23.99,  8,  80, 160, 99.9, 4],
    ["MCProHosting", "Gold", 47.99, 16, 160, 320, 99.9, 4],

    # Sparked Host
    ["Sparked Host", "Basic",   1.00,  2,  20,  40, 99.9, 1],
    ["Sparked Host", "Standard",6.00,  4,  40,  80, 99.9, 2],
    ["Sparked Host", "Pro",    12.00,  8,  80, 160, 99.9, 4],
    ["Sparked Host", "Elite",  24.00, 16, 160, 320, 99.9, 4],

    # Hostinger
    ["Hostinger", "Panel1",  6.99,  4,  50,  80, 99.9, 1],
    ["Hostinger", "Panel2",  9.49,  8, 100, 160, 99.9, 2],
    ["Hostinger", "Panel4", 13.99, 16, 200, 320, 99.9, 4],
    ["Hostinger", "Panel8", 27.99, 32, 400, 640, 99.9, 8],

    # Nodecraft Budget (Lite — hibernates)
    ["Nodecraft", "Lite2GB",   5.96,  2,  20,  40, 99.9, 1],
    ["Nodecraft", "Lite4GB",  11.92,  4,  40,  80, 99.9, 1],
    ["Nodecraft", "Lite8GB",  23.84,  8,  80, 160, 99.9, 2],
    ["Nodecraft", "Lite16GB", 47.68, 16, 160, 320, 99.9, 4],

    # Nodecraft Premium (24/7)
    ["Nodecraft", "Prem2GB",   9.98,  2,  20,  40, 99.9, 1],
    ["Nodecraft", "Prem4GB",  19.98,  4,  40,  80, 99.9, 2],
    ["Nodecraft", "Prem8GB",  39.98,  8,  80, 160, 99.9, 4],
    ["Nodecraft", "Prem16GB", 79.98, 16, 160, 320, 99.9, 4],

    # GGServers
    ["GGServers", "Basic",    3.00,  2,  20,  12, 99.9, 1],
    ["GGServers", "Standard", 6.00,  4,  40,  24, 99.9, 2],
    ["GGServers", "Premium", 12.00,  8,  80,  48, 99.9, 4],

    # Akliz
    ["Akliz", "Standard", 4.50, 2,  30,  40, 99.9, 1],
    ["Akliz", "Advanced", 8.50, 4,  60,  80, 99.9, 2],
    ["Akliz", "Premium", 16.00, 8, 120, 160, 99.9, 4],

    # Godlike.host
    ["Godlike.host", "Basic",   6.39,  2,  20,  40, 99.9, 2],
    ["Godlike.host", "Standard",12.79, 4,  40,  80, 99.9, 2],
    ["Godlike.host", "Pro",    25.59,  8,  80, 160, 99.9, 4],
    ["Godlike.host", "Elite",  64.99, 32, 320, 640, 99.9, 8],

    # Host Havoc
    ["Host Havoc", "Basic",    4.00,  2,  20,  40, 99.9, 1],
    ["Host Havoc", "Standard", 8.00,  4,  40,  80, 99.9, 2],
    ["Host Havoc", "Advanced",16.00,  8,  80, 160, 99.9, 4],

    # ServerMiner
    ["ServerMiner", "Basic",    5.00,  2,  20,  40, 99.9, 1],
    ["ServerMiner", "Standard",10.00,  4,  40,  80, 99.9, 2],
    ["ServerMiner", "Premium", 20.00,  8,  80, 160, 99.9, 4],

    # G-Portal
    ["G-Portal", "Basic",    4.85,  2,  30,  40, 99.9, 1],
    ["G-Portal", "Standard", 9.70,  4,  60,  80, 99.9, 2],
    ["G-Portal", "Premium", 19.40,  8, 120, 160, 99.9, 4],

    # exaroton (pay-as-you-go, by Aternos)
    ["exaroton", "PayGo", 10.00, 4,  10,  80, 99.5, 2],

    # Pine Hosting
    ["Pine Hosting", "Standard", 4.20, 2,  30,  40, 99.8, 1],

    # CloudNord
    ["CloudNord", "Basic", 5.00, 2,  20,  40, 99.9, 1],
]

columns = [
    "Platform", "Tier", "Harga (USD/mo)", "RAM (GB)",
    "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"
]

df = pd.DataFrame(data, columns=columns)

# --- OUTPUT: Excel ---
df.to_excel("Dokumen/Dataset_Hosting_Minecraft.xlsx", index=False, sheet_name="Data Hosting")
print("[OK] Excel: Dokumen/Dataset_Hosting_Minecraft.xlsx")

# --- OUTPUT: CSV ---
df.to_csv("Dokumen/Dataset_Hosting_Minecraft.csv", index=False)
print("[OK] CSV  : Dokumen/Dataset_Hosting_Minecraft.csv")

# --- RINGKASAN ---
print(f"\n== Total baris : {len(df)}")
print(f"== Total platform unik : {df['Platform'].nunique()}")
print(f"== Kolom : {', '.join(columns)}")
print(f"\nDistribusi per platform:")
for p, c in df.groupby("Platform").size().items():
    print(f"  {p}: {c} tier")
