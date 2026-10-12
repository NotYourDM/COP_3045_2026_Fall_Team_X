import pandas
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns

import src.data.data_merger as data_merger

PATH : str = "src/report/"

def make_pdf(path : str, df : pandas.DataFrame, include : dict[str, bool]) -> None:
    print()
    input("---------- Generating PDF Report ----------")
    print()

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Times", "B", 20)
    pdf.cell(0, 12, "Movie Statistics - Automated Report", ln=True, align='C')
    pdf.ln(10)

    if include["merge"]:
        input("Adding merge info...")
        pdf.set_font("Times", "B", 15)
        pdf.cell(0, 30, "Dataset Merge Process")
        pdf.ln(30)

        pdf.set_font("Times", "", 9)
        pdf.cell(0, 8, "Datasets {movie_info.csv} and {movie_ratings.csv} were merged into {movie_data.csv}.")
        pdf.ln(5)
        successes, failures, percentage, headers = data_merger.get_merge_stats()
        pdf.cell(0, 8, f"A total of {successes} movies were successfully merged.")
        pdf.ln(5)
        pdf.cell(0, 8, f"A total of {failures} movies were unable to be matched.")
        pdf.ln(5)
        pdf.cell(0, 8, f"({percentage:.2f}%)")
        pdf.ln(5)

        pdf.cell(0, 8, "Merged Categories:")
        pdf.ln(10)

        for i in range(len(headers)):
            pdf.cell(0, 8, headers[i])
            pdf.ln(5)

        pdf.add_page()
        input("Merge info complete.")




    if include["clean"]:
        input("Adding cleanliness report...")
        pdf.set_font("Times", "B", 15)
        pdf.cell(0, 30, "Data Cleanliness Report")
        pdf.ln(5)

        clean_check = pandas.DataFrame( 
            (["Total Rows", "Total Columns", "Duplicate Rows", "Missing Values"], 
             [df.shape[0], df.shape[1], df.duplicated().sum(), df.isna().sum().sum()])
        )

        df_to_pdf_table(clean_check, pdf, "", 5, 50)
        pdf.add_page()
        input("Cleanliness complete.")

    if include["summary"]:
        input("Adding summary statistics...")
        pdf.set_font("Times", "B", 15)
        pdf.cell(0, 30, "Summary Statistics")
        pdf.ln(5)

        df_to_pdf_table(df.describe(), pdf, "", 5, 50)
        pdf.add_page()
        input("Summary complete.")

    if include['visual']:
        input("Adding visual components...")
        plt.figure(figsize=(10, 5))
        sns.histplot(df["revenue"])
        plt.title("Revenue Distribution")
        plt.xscale("log")
        plt.tight_layout()
        plt.savefig(PATH + "revenue_dist.png")
        plt.close()

        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=df, x="budget", y="revenue")
        plt.title("Budget vs Revenue")
        plt.xscale("log")
        plt.yscale("log")
        plt.tight_layout()
        plt.savefig(PATH + "budget_vs_revenue.png")
        plt.close()
    
        plt.figure(figsize=(25, 15))
        sns.boxplot(data=df, x="genres", y="audience_rating_%")
        plt.title("Genres vs Audience Rating %")
    
        tick_trim : int = 4
        xticks, xlabels = plt.xticks()
        plt.xticks(ticks=xticks[::tick_trim], rotation=45, horizontalalignment="right", labels=xlabels[::tick_trim], fontsize=8)
        
        plt.savefig(PATH + "genres_vs_ratings.png")
        plt.close()

        pdf.set_font("Times", "B", 15)
        pdf.cell(0, 25, "Visualizations")
        pdf.ln(5)
        pdf.image(PATH + "revenue_dist.png", x=10, y=40, w=180)
        pdf.image(PATH + "budget_vs_revenue.png", x=10, y=125, w=180)
        pdf.image(PATH + "genres_vs_ratings.png", x=10, y=170, w=190)
        input("Visuals complete.")

    print(f"Outputting to... {PATH+path}")
    pdf.output(PATH + path)

    print("--------------------")

def df_to_pdf_table(df : pandas.DataFrame, pdf : FPDF, name : str = "", x : int = -1, y : int = -1) -> None:
    df = df.round(2).rename_axis(name).reset_index()
    rows = [df.columns.astype(str).tolist()]
    rows += df.astype(str).values.tolist()

    if (x != -1) and (y != -1):
        pdf.set_xy(x, y)
    pdf.set_font("Times", "", 9)
    
    with pdf.table(text_align="CENTER") as table:
        for df_row in rows:
            row = table.row()
            for value in df_row:
                row.cell(value)

