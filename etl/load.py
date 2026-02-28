from database.connection import engine


def load_data(df):
    print("Loading data into database...")
    df.to_sql("player_stats", engine, if_exists="replace", index=False)
    print("Data loaded successfully.")