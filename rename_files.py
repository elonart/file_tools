import os
import os.path

#
# Usage:
# python rename_files.py
#

# < < Change base info > >
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"

def rename_files():
    source_dir = WAKIME_DOC
    i = 1
    files = os.listdir(source_dir)
    files.sort()
    for filename in files:
        oldFile = os.path.join(source_dir, filename)
        newFile = os.path.join(source_dir, "%03d%s" % (i, ".jpg"))
        os.rename(oldFile, newFile)
        i += 1

if __name__ == '__main__':
    rename_files()
