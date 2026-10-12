import src.eda.summary_stats as summary_stats
import src.eda.visualization as visualization
import src.eda.pdf_export as pdf_export
import pandas


def display_data(df: pandas.DataFrame, include_summary : bool, include_visualization : bool, include_pdf_export : bool) -> None:
    if include_summary:
        summary_stats.get_summary_stats(df)
    if include_visualization:
        visualization.make_plots(df)


