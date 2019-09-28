import os
import os.path

#
# Usage:
# python change_file_ext.py
#

# < < Change base info > >
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"
source_dir = WAKIME_DOC + "/annotation/image"


def change_file_ext():
    files = os.listdir(source_dir)
    for filename in files:
        oldFile = os.path.join(source_dir, filename)
        extension = os.path.splitext(filename)[1]
        if extension == ".JPG":
            extension = ".jpg"
            newFile = os.path.join(source_dir, os.path.splitext(filename)[0] + extension)
            os.rename(oldFile, newFile)

if __name__ == '__main__':
    change_file_ext()
