import pathlib
'''
1. Write the following text to a file in your home directory called
starships.txt:
Discovery
Enterprise
Defiant
Voyager
Each word should be on a separate line.
'''
ships = [
    "Discovery\n",
    "Enterprise\n",
    "Defiant\n",
    "Voyager\n"
]

starship_file = pathlib.Path.cwd() / 'starships.txt'
if not starship_file.exists():
    starship_file.touch()

with starship_file.open(mode="w", encoding="utf-8") as file:
    file.writelines(ships)
'''
2. Read the file starhips.txt that you created in exercise 1 and print
each line of text in the file. The output should not have extra blank
lines between each word.
'''
print('Read the file and output each line of text!')
with starship_file.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line,end='')

'''
3. Read the file startships.txt and print the names of the starships
that start with the letter D.
'''
print('Print the name of the starships that start with the letter D!')
with starship_file.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        if line.startswith('D'):
            print(line, end="")