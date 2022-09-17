'''
In the chapter 12 practice_files folder, there is a subfolder called
documents/. The directory contains several files and subfolders. Some
of the files are images ending with the .png, .gif, or .jpg file extension.
Create a new folder in the practice_files folder called images/, and
move all image files to that folder. When you’re done, the new folder
should have four files in it:
1. image1.png
2. image2.gif
3. image3.png
4. image4.jpg
'''

# Libraries
import pathlib

# grab path to pratice documents folder
# Make sure to move the practice files found in the books 
# github repository https://github.com/realpython/python-basics-exercises
# To the same directory as this script
practice_dir = pathlib.Path.cwd() / 'practice_files' / 'documents'

# Images folder path creation
images_dir = pathlib.Path.cwd() / 'practice_files' / 'images'
if not images_dir.exists():
    images_dir.mkdir() 

# search for image files with extensions: gif, png, jpg
# Reference https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob
img_ext = ['*.gif','*.png','*.jpg']

# Recursively search for image files with the above extension list 
for images in img_ext:
    for path in practice_dir.rglob(images):
        # Move images found to images directory
        destination = images_dir / path.name
        if not destination.exists():
            path.replace(destination)

