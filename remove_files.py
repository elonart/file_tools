import os
import os.path

#
# Usage:
# python remove_files.py
#

# < < Change base info > >
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"
source_dir = WAKIME_DOC + "/annotation/YOLO_File"

def remove_files():    
    files = os.listdir(source_dir)
    for filename in files:
        extension = os.path.splitext(filename)[1]
        if extension in (".jpg", ".JPG"):
            filename = os.path.join(source_dir, filename)
            os.remove(filename)

if __name__ == '__main__':
    remove_files()
