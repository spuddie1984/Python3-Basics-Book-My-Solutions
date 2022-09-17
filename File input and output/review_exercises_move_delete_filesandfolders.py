import shutil
import pathlib

# 1. Create a new directory in your home folder called my_folder/.

new_dir = pathlib.Path.home() / "my_folder"
if not new_dir.exists():
    new_dir.mkdir()
else:
    print(f"Sorry the path {new_dir} already exists")

'''
2. Inside my_folder/ create three files:
    • file1.txt
    • file2.txt
    • image1.png
'''

paths = [
    new_dir / "file1.txt",
    new_dir / "file2.txt",
    new_dir / "image1.png",
]

for path in paths:
    if not path.exists():
        path.touch()
    else:
        print(f"Sorry the file {path} already exists!!")

'''
3. Move the file image1.png to a new directory called images/ inside the
my_folder/ directory.
'''
source = new_dir / "image1.png"
destination_dir = new_dir / "images"
destination = new_dir / "images" / "image1.png"

if not destination.exists():
    destination_dir.mkdir()
    source.replace(destination)
else:
    print(f"Sorry the destination file {destination} already exists, please try delete it and try again!!")


# 4. Delete the file file1.txt.

file1 = new_dir / "file1.txt"
if file1.exists():
    file1.unlink()
    print(f"File {file1} is deleted!!")


# 5. Delete the my_folder/ directory.

'''
If you need to delete an entire directory even if it’s non-empty, then
pathlib won’t help you much. However, the built-in shutil module
includes a rmtree() function that you can use to delete directories pop-
ulated with files.
'''

if not new_dir.exists():
    shutil.rmtree(new_dir)