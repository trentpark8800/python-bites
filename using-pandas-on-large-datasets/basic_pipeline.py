import tracemalloc
import json

import pandas as pd

def data_cleaning(df):
    """Fill blank and or missing values"""
    df = df.fillna(0)

    return df


def lead_time_filter(df, filter_value):
    """Only keep the lead time values above the median"""

    filtered_df = df[df["lead_time"] >= filter_value].copy()
    return filtered_df


def extract(file_path):
    """Extract the data from the csv file into a dataframe"""
    df_chunks = pd.read_csv(
    "./data/hotel_bookings.csv",
    usecols= [
            "hotel",
            "arrival_date_year",
            "arrival_date_month",
            "arrival_date_day_of_month",
            "adults",
            "children",
            "babies",
            "customer_type",
            "is_canceled",
            "lead_time",
        ],
        chunksize=1000
    )
    return df_chunks


def transform(df, schema):
    """Apply the transformation steps to the data"""
    df = data_cleaning(df)

    df = df.astype(schema)

    filtered_df = lead_time_filter(df, filter_value=50)

    return filtered_df


def load(filtered_df, output_path):
    """Write the dataframes to csv files"""

    filtered_df.to_csv(f"{output_path}/high_lead_time_bookings.csv", index=False, mode='a')


def main():

    tracemalloc.start()

    with open("./schema.json") as f:
        schema = json.load(f)
        f.close()

    file_path = "./data/hotel_bookings.csv"
    for df in extract(file_path):

        filtered_df = transform(df, schema)

        load(filtered_df, "./data/")

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6} MB; Peak was {peak / 10**6} MB")
    tracemalloc.stop()


if __name__ == "__main__":
    main()
