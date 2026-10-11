import os
import csv

PATH = "src/data/"

class Movie:
    def __init__(self):
        pass


def merge_files(path_1 : str, path_2 : str) -> None:
    input("Starting to read file 1.")

    with open(path_1, 'r') as file:
        data = csv.DictReader(file)

        if data:
            input("File 1 read.")

        for key in data:
            input(key)
    input("File 1 done.")
    

    input("Starting to read file 2.")

    with open(path_2, 'r') as file:
        data = csv.DictReader(file)

        if data:
            input("File 2 read.")

        for key in data:
            input(key)
    input("File 2 done.")


if __name__ == "__main__":
    print("Files: ")
    for f in os.listdir(PATH):
        print(f)
    file_to_read_1 = input("Pick CSV file 1: ")
    file_to_read_2 = input("Pick CSV file 2: ")
    merge_files(PATH + file_to_read_1, PATH + file_to_read_2)


