import src.data.data_merger as data_merger
import src.data.data_clean_check as data_clean_check
import pandas

def get_data_frame(include_merge : bool = False, include_clean_report : bool = False) -> pandas.DataFrame:
    if include_merge:
        data_merger.merge_files()
    df : pandas.DataFrame = data_clean_check.get_clean_df(include_clean_report)
    return df

