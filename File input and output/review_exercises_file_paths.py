import pathlib

'''
1. Create a new Path object to a file called my_file.txt in a folder called
my_folder/ in your computer’s home directory. Assign this Path ob-
ject to the variable name file_path .
'''
file_path = pathlib.Path('/my_folder/my_file.txt')
'''
2. Check whether the path assigned to file_path exists.
'''
print(file_path.exists())
'''
3. Print the name of the path assigned to file_path.
The output should be my_file.txt.
'''
print(file_path.name)
'''
4. Print the name of the parent directory of the path assigned to
file_path. The output should be my_folder.
'''
print(file_path.parent)