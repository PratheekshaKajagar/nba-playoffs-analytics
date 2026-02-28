import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Transforming data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert hall_of_fame to binary
    df["hall_of_fame"] = df["hall_of_fame"].notna().astype(int)
    # Convert numeric columns safely
    numeric_cols = [
        "total_points",
        "total_games",
        "field_goals",
        "three_points_goals",
        "free_shots"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Feature Engineering
    df["points_per_game"] = df["total_points"] / df["total_games"]
    df["three_point_ratio"] = df["three_points_goals"] / df["field_goals"]
    df["free_throw_ratio"] = df["free_shots"] / df["field_goals"]

    df = df.fillna(0)

    print("Transformation complete.")
    return df