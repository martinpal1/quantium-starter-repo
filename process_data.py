import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_FILE = DATA_DIR / "formatted_output.csv"

# Load all CSV files from the data folder
csv_files = list(DATA_DIR.glob("*.csv"))

frames = []

for file in csv_files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Clean price field and convert to number
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

    # Calculate sales
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns to required output format
    df = df.rename(columns={
        "date": "Date",
        "region": "Region"
    })

    frames.append(df)

# Combine all three CSVs
output = pd.concat(frames, ignore_index=True)

# Save output
output.to_csv(OUTPUT_FILE, index=False)

print(f"Created {OUTPUT_FILE}")