import matplotlib.pyplot as plt
import seaborn as sns
import pandas

import random

boxplot_genres : list[int] = []
all_genres : list = []


def make_plots(df : pandas.DataFrame) -> None:
    print()
    input("---------- Visualizing Data ----------")
    print()

    _, plots = plt.subplots(1, 2, figsize=(10, 5))

    input("Preparing plots: Revenue Distribution (Histplot) + Budget vs Revenue (Scatterplot)")
    sns.histplot(df["revenue"], ax=plots[0])
    plots[0].set_title("Revenue Distribution")
    plots[0].set_xscale("log")

    sns.scatterplot(data=df, x="budget", y="revenue", ax=plots[1])
    plots[1].set_title("Budget vs Revenue")
    plots[1].set_xscale("log")
    plots[1].set_yscale("log")
    print()

    _, boxplot = plt.subplots(1, 1, figsize=(35, 7))

    input("Preparing plot: Genres vs Audience Rating % on a separate window.")
    sns.boxplot(data=df, x="genres", y="audience_rating_%", ax=boxplot)
    boxplot.set_title("Genres vs Audience Rating %")
    
    print()
    print("A 'tick trimming factor' needs to be chosen. This value will be used to reduce the number of visible grid ticks and labels.")
    print("(For example, a tick trimming factor of '5' means that for every 5 ticks, only one will be displayed on screen.")
    print(" This is because there is a large amount of movie genres.")
    print(" Regardless of the tick trimming factor, all elements of the box plot will be displayed onscreen.)")

    tick_trim : int = -1
    while (tick_trim <= 0):
        try:
            tick_trim = int(input("Enter tick trimming factor (whole number greater than 0): "))
        except:
            print("This input does not appear to be a number.")
        if tick_trim <= 0:
            print("This input appears to be less than or equal to 0")

    # boxplot_choose_genres(df)
    boxplot.set_xticks(ticks=boxplot.get_xticks()[::tick_trim], rotation=45, horizontalalignment="right", labels=boxplot.get_xticklabels()[::tick_trim])

    plt.tight_layout()
    plt.show()
    print("--------------------")



# Unused genre choosing system
def boxplot_choose_genres(df : pandas.DataFrame) -> None:
    global all_genres

    print("Choose genres for the boxplot.")
    print("(Any related genre to the one you choose will be added as well.")
    print(" for example: 'Action' will include 'Action Adventure' and 'Action Comedy')")
    print()
    print("If you do not want to choose a genre, enter 'RANDOM' instead.")
    print()
    print("When you are done choosing genres, enter 'STOP' and the plots will display.")
    print()
    print("If you would like to remove a genre, enter 'DELETE [x]' to delete the xth element (counts from 1).")
    print()

    all_genres = df["genres"].tolist()

    choosing_genres : bool = True
    while choosing_genres:
        print("These are the current genres (recommended no more than 5-10):")
        print()

        print("-------")
        for g in boxplot_genres:
            print(all_genres[g])
        print("-------")
        
        genre_prompt : str = input("Choose a genre, RANDOM, DELETE [x], or STOP: ")
        choosing_genres = execute_genre_prompt(genre_prompt)
        print()
    input("Done.")
    print("Displaying Boxplot...")


def execute_genre_prompt(prompt : str) -> bool:
    if prompt == 'STOP':
        return False
    
    prompt = prompt.lower()

    if prompt[0:6] == 'delete':
        to_remove : int = int(prompt[7:])
        print(f"Removing: {all_genres[boxplot_genres.pop(to_remove - 1)]}")
        return True

    if prompt == 'random':
        idx : int = random.randint(0, len(all_genres)-1)
        boxplot_genres.append(idx)
        print("Adding random genre: " + all_genres[idx])
        return True

    for i in range(len(all_genres)):
        genre : str = all_genres[i]
        if prompt in genre.lower():
            boxplot_genres.append(i)
            print(f"Adding: {genre}")


    return True

