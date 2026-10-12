import matplotlib.pyplot as plt
import seaborn as sns
import pandas

def make_plots(df : pandas.DataFrame) -> None:
    sns.histplot(df["revenue"])
    plt.title("Revenue")
    plt.show()

    sns.scatterplot(data=df, x="budget", y="revenue")
    plt.xscale("log")
    plt.yscale("log")

    sns.boxplot(data=df, x="genres", y="audience_rating_%")

