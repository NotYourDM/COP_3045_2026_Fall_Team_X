import matplotlib.pyplot as plt
import seaborn as sns
import pandas

def make_plots(df : pandas.DataFrame) -> None:
    figure, plots = plt.subplots(1, 3, figsize=(10, 5), gridspec_kw={"width_ratios": [3, 3, 6]})

    sns.histplot(df["revenue"], ax=plots[0])
    plots[0].set_title("Revenue Distribution")
    plots[0].set_xscale("log")

    sns.scatterplot(data=df, x="budget", y="revenue", ax=plots[1])
    plots[1].set_title("Budget vs Revenue")
    plots[1].set_xscale("log")
    plots[1].set_yscale("log")

    sns.boxplot(data=df, x="genres", y="audience_rating_%", ax=plots[2])
    plots[2].set_title("Genres vs Audience Rating %")

    print(plots[2].get_xticklabels())
    plots[2].set_xticks(ticks=plots[2].get_xticks()[::30], rotation=45, horizontalalignment="right", labels=plots[2].get_xticklabels()[::30])

    plt.show()
