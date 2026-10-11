import os
import csv
import json

PATH = "src/data/"

class Movie:
    def __init__(self, title : str, ):
        pass


def merge_files(path_1 : str, path_2 : str) -> None:
    input(f"Reading files: {path_1} and {path_2}")
    data_1 = []

    with open(path_1, 'r') as file:
        dict_reader = csv.DictReader(file)

        for row in dict_reader:
            data_1.append(row)
    input(f"{path_1} done.")

    input(f"Starting to read {path_2}")
    data_2 = []

    with open(path_2, 'r') as file:
        dict_reader = csv.DictReader(file)

        for row in dict_reader:
            data_2.append(row)
    input(f"{path_2} done.")

    input("Matching movies:")
    data_merge = []

    success_count : int = 0
    fail_count : int = 0

    for movie_1 in data_1:
        movie_1_name = (movie_1["Film"].strip()).lower()
        movie_1_year = (movie_1["Year of release"])

        match_success = False

        for movie_2 in data_2:
            movie_2_name = (movie_2["title"].strip()).lower()

            #movie_2_year = movie_2["release_date"]
            #if movie_2_year == '':
            #    if movie_1_name == movie_2_name:
            #        input("Successful match: "+movie_1_name + " and "+movie_2_name)
            #        success_count += 1
            #        break
            #    else:
            #        fail_count += 1
            #movie_2_year = int(movie_2["release_date"][0:4])

            if movie_1_name == movie_2_name: # and movie_1_year == movie_2_year:

                movie = movie_2
                movie["release_date"] = movie_1_year

                data_merge.append(movie)

                success_count += 1
                match_success = True

                data_2.remove(movie_2)
                break

        if not match_success:
            print("Unable to match: " + movie_1_name)
            fail_count += 1

    new_path : str = PATH + "movie_data.json"
    
    input(f"Editing / creating file at: {new_path}")
    with open(new_path, 'w') as file:
        file.write(json.dumps(data_merge))
    input(f"Wrote merged data to {new_path}")

    input(f"Successfully merged {success_count} movies.")
    input(f"Failed to merge {fail_count} movies.")
    input(f"Success rate: { (success_count / (success_count + fail_count) * 100.0) }%")


if __name__ == "__main__":
    print("Files: ")
    for f in os.listdir(PATH):
        print(f)
    file_to_read_1 = "movie_ratings.csv"
    file_to_read_2 = "movie_data.csv"
    merge_files(PATH + file_to_read_1, PATH + file_to_read_2)


