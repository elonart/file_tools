import os
import os.path
import cv2
from decimal import Decimal

#
# Usage:
# python rotate_images.py
#

# < < Change base info > >
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"
source_dir = WAKIME_DOC + "/annotation/YOLO_File"
txt_src = WAKIME_DOC + "/annotation/txt"
txt_dest = WAKIME_DOC + "/annotation/txt_changed/CRLF"


def get_portrait_images():
    portrait_images = []
    files = os.listdir(source_dir)
    #files.sort()
    for filename in files:
        basename = os.path.splitext(filename)[0]
        filepath = os.path.join(source_dir, filename)
        im = cv2.imread(filepath)
        height, width, channels = im.shape
        if width < height:
            portrait_images.append(basename)

    return portrait_images


def rotate_images():
    portrait_images = get_portrait_images()
    files = os.listdir(txt_src)
    for filename in files:
        basename = os.path.splitext(filename)[0]
        filepath = os.path.join(txt_src, filename)
        dest_file = os.path.join(txt_dest, filename)
        with open(filepath) as fp:
            with open(dest_file, "w") as df:
                lines = fp.readlines()
                for line in lines:
                    items = line.split()
                    if basename in portrait_images:                        
                        changed_items = [items[0], str(Decimal(1) - Decimal(items[2])), items[1], items[4], items[3]]
                    else:
                        changed_items = items
                    
                    for i in range(len(changed_items)):
                        if i == len(changed_items) - 1:
                            df.write(changed_items[i])
                        else:
                            df.write(changed_items[i] + " ")
                    df.write("\n")
        
        
if __name__ == '__main__':
    rotate_images()
