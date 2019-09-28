import os
import os.path

#
# Usage:
# python change_files.py
#

# < < Change base info > >
REPLACE_CLASS_ID = str(0)
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"
source_dir = WAKIME_DOC + "/annotation/class"
dest_dir = WAKIME_DOC + "/annotation/new_class"


def change_files():
    files = os.listdir(source_dir)
    for filename in files:
        filepath = os.path.join(source_dir, filename)
        with open(filepath) as fp:
            dest_file = os.path.join(dest_dir, filename)
            with open(dest_file, "w") as df:
                lines = fp.readlines()
                for line in lines:
                    items = line.split()
                    items[0] = REPLACE_CLASS_ID
                    for i in range(len(items)):
                        if i == len(items) - 1:
                            df.write(items[i])
                        else:
                            df.write(items[i] + " ")
                    df.write("\n")

if __name__ == '__main__':
    change_files()
