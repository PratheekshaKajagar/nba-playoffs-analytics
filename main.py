from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_pipeline():
    df = extract_data("data/nba_playoffs.csv")
    df_transformed = transform_data(df)
    load_data(df_transformed)


if __name__ == "__main__":
    run_pipeline()