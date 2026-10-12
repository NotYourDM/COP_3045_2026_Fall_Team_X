import os
import csv
from typing import Literal

PATH = "src/data/"


def read_file(path : str) -> list:
    input(f"Starting to read {path}")
    _data = []

    with open(path, 'r') as file:
        dict_reader = csv.DictReader(file)

        for row in dict_reader:
            _data.append(row)
    input(f"Finished reading {path}")
    return _data


def write_file_csv(path : str, data : list) -> None:
    input(f"Writing to file at: {path}")
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    input(f"Wrote merged data to {path}")


def merge_files(path_1 : str, path_2 : str) -> None:
    data_1 : list = read_file(path_1)
    data_2 : list = read_file(path_2)

    input("Matching movies...")

    # This file merge system basically takes all the properties that exist in the larger dataset 2, and adds the corresponding dataset 1's
    # rating information.

    headers : list[str] = ["index", "budget", "genres", "homepage", "id", "keywords", "original_language", "original_title", 
               "overview", "popularity", "production_companies", "production_countries", "release_date", "revenue", "runtime", 
               "spoken_languages", "status", "tagline", "title", "vote_average", "vote_count", "cast", "crew", "director"]

    # Headers_to_merge must be the name of the actual headers in dataset 1.
    # The alias will be the new header names assigned in the merged dataset.
    # This is because the naming conventions are different across the datasets, so we can enforce consistent naming using this alias system.
    headers_to_merge : list[str] = ["Rotten Tomatoes Ratings %", "Audience Ratings %"]
    headers_to_merge_alias : list[str] = ["rotten_tomatoes_rating_%", "audience_rating_%"]

    headers = headers + headers_to_merge_alias
    
    data_merge : list = []

    success_count : int = 0
    fail_count : int = 0

    for movie_1 in data_1:
        movie_1_name = (movie_1["Film"].strip()).lower()
        movie_1_year = (movie_1["Year of release"])

        match_success = False

        for movie_2 in data_2:
            movie_2_name = (movie_2["title"].strip()).lower()

            if movie_1_name == movie_2_name:
                # print("Successful match: " + movie_1_name)  # (this will say every movie that did match)

                movie_2["release_date"] = movie_1_year

                movie_merge = []

                for i in range(len(headers_to_merge)):
                    movie_2[headers_to_merge_alias[i]] = movie_1[headers_to_merge[i]]

                for header in headers:
                    if header in headers_to_merge:
                        movie_2[header] = movie_1[header]
                    movie_merge.append( movie_2[header] )

                data_merge.append(movie_merge)

                success_count += 1
                match_success = True

                data_2.remove(movie_2)
                break

        if not match_success:
            # print("Unable to match: " + movie_1_name)  # (this will say every single movie that failed to match)
            fail_count += 1
    input("Matching complete.")

    data_merge = [headers] + data_merge
    
    write_file_csv(PATH + "movie_data.csv", data_merge)

    input(f"Successfully merged {success_count} movies.")
    input(f"Failed to merge {fail_count} movies.")
    input(f"Success rate: {(success_count / (success_count + fail_count) * 100.0):.2f}%")
    input("Note that these values may include duplicates. Those will be removed in the file cleaning process.")


if __name__ == "__main__":
    print("Files to merge: ")
    file_to_read_1 = "movie_ratings.csv"
    file_to_read_2 = "movie_info.csv"
    merge_files(PATH + file_to_read_1, PATH + file_to_read_2)


