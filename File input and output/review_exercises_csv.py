import csv
import pathlib

'''
1. Write a program that writes the following list of lists to a file in
your home directory called numbers.csv:
'''

numbers = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]

file_path = pathlib.Path.home() / 'numbers.csv'

with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for number in numbers:
        writer.writerow(number)
'''
2. Write a program that reads the numbers in the numbers.csv file
from exercise 1 into a list of lists of integers called numbers. Print
the list of lists. Your output should look like this:
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
'''
list_of_lists = []
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        list_of_lists.append([value for value in row])

print(list_of_lists)
'''
3. Write a program that writes the following list of dictionaries to a
file in your home directory called favorite_colors.csv:
favorite_colors = [
{"name": "Joe", "favorite_color": "blue"},
{"name": "Anne", "favorite_color": "green"},
{"name": "Bailey", "favorite_color": "red"},
]
The output CSV file should have the following format:
name,favorite color
Joe,blue
Anne,green
Bailey,red
'''

fav_col_file_path = pathlib.Path.home() / 'favourite_colors.csv'

with fav_col_file_path.open(mode="w", encoding="utf-8", newline="") as file:
    pass

'''
4. Write a program that reads the data from the favorite_colors.csv
file from exercise 3 into a list of dictionaries called favorite_colors.
Print the list of dictionaries. The output should look something
like this:
[{"name": "Joe", "favorite_color": "blue"},
{"name": "Anne", "favorite_color": "green"},
{"name": "Bailey", "favorite_color": "red"}]
'''