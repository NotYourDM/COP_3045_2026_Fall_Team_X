import pandas
import sys

print(sys.executable)

PATH = "src/data/"

def clean_check() -> None:
    df = pandas.read_csv(PATH + "movie_data.csv")

    input(f"Missing values:\n{df.isna().sum()}")
    input(f"Duplicated rows:\n{df.duplicated().sum()}")
    input(f"Data types:\n{df.dtypes}")

    if df.duplicated.any():
        df = df.drop_duplicates()
