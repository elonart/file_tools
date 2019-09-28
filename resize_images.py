import os
import os.path
import cv2

#
# Usage:
# python resize_images.py
#

# < < Change base info > >
IN_SIZE=416
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"
source_dir = WAKIME_DOC + "/annotation/YOLO_File"
dest_dir = WAKIME_DOC + "/annotation/resized/"

def resize_images():
    files = os.listdir(source_dir)
    for filename in files:
        basename = os.path.splitext(filename)[0]
        filepath = os.path.join(source_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        im = cv2.imread(filepath)
        height, width, channels = im.shape
        aspect_ratio = width / height
        if width < height:
            width = IN_SIZE
            height = int(width / aspect_ratio)
        else:
            height = IN_SIZE
            width = int(height * aspect_ratio)

        dim = (width, height)
        resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(dest_file, resized)

if __name__ == '__main__':
    resize_images()