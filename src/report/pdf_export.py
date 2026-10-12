import pandas
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns

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

    row_count, column_count = df.shape

    if include['merge']:
        pass

    if include['clean']:
        pass

    if include["summary"]:
        input("Adding summary statistics...")
        pdf.cell(0, 10, "Summary Statistics")
        pdf.ln(5)
        pdf.cell(0, 100, str(df.describe()), 1)
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
    
        plt.figure(figsize=(25, 8))
        sns.boxplot(data=df, x="genres", y="audience_rating_%")
        plt.title("Genres vs Audience Rating %")
    
        tick_trim : int = 4
        xticks, xlabels = plt.xticks()
        plt.xticks(ticks=xticks[::tick_trim], rotation=45, horizontalalignment="right", labels=xlabels[::tick_trim], fontsize=8)
        
        plt.savefig(PATH + "genres_vs_ratings.png")
        plt.close()

        pdf.cell(0, 10, "Visualizations")
        pdf.ln(5)
        pdf.image(PATH + "revenue_dist.png", x=10, y=10, w=180)
        pdf.image(PATH + "budget_vs_revenue.png", x=10, y=200, w=180)
        
        pdf.add_page()
        pdf.image(PATH + "genres_vs_ratings.png", x=10, y=10, w=180)
        input("Visuals complete.")

    print(f"Outputting to... {PATH}project_report.pdf")
    pdf.output(PATH + "project_report.pdf")

    print("--------------------")


    

