import pandas

def get_summary_stats(df : pandas.DataFrame) -> None:
    input("Getting summary stats.")
    columns : list[str] = ["budget", "revenue", "runtime", "popularity", "vote_average", "vote_count", "rotten_tomatoes_rating_%", "audience_rating_%"]
    print(df[columns].describe())
