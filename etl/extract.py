import pandas as pd


def extract_data(file_path: str) -> pd.DataFrame:
    print("Extracting data...")
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows.")
    return df