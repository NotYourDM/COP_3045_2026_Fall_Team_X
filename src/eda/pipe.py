import src.eda.summary_stats as summary_stats
import src.eda.visualization as visualization
import src.eda.pdf_export as pdf_export
import pandas


def display_data(df: pandas.DataFrame) -> None:
    summary_stats.get_summary_stats(df)
    visualization.make_plots(df)


