import pandas

PATH = "src/data/"

def get_clean_df(print_unclean : bool = False) -> pandas.DataFrame:
    df : pandas.DataFrame = pandas.read_csv(PATH + "movie_data.csv")

    if print_unclean:
        print_df_issues()

    if df.duplicated().any():
        df = df.drop_duplicates()
    return df


def print_df_issues() -> None:
    print()
    input("---------- Checking File Cleanliness ----------")
    print()
    input(f"Missing values:\n{df.isna().sum()}")
    input(f"Duplicated rows:\n{df.duplicated().sum()}")
    input(f"Data types:\n{df.dtypes}")
    print("--------------------")

