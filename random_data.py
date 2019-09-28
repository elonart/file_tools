import os
import os.path
import random
#
# Usage:
# python random_data.py
#

# < < Change base info > >
WAKIME_DOC = "C:/Users/gow/Documents/Wakime"
dest_dir = WAKIME_DOC + "/annotation/result"
UNIX_LINE_ENDING = b'\n'
DATA_VOLUME = 374
SEED_VALUE = 9
CUT_POINT = 288
# if use rate...
# CUT_POINT = int(DATA_VOLUME * 0.7)


def random_data():
    data_list = [i + 1 for i in range(DATA_VOLUME)]
    random.seed(SEED_VALUE)
    random.shuffle(data_list)

    train_file = os.path.join(dest_dir, "train.txt")
    test_file = os.path.join(dest_dir, "test.txt")

    train_list = []
    for i in range(CUT_POINT):
        train_list.append(data_list[i])    
    train_list.sort()

    test_list = []
    for i in range(CUT_POINT, DATA_VOLUME):
        test_list.append(data_list[i])    
    test_list.sort()
   
    with open(train_file, "wb") as tf:
        for i in range(len(train_list)):
            tf.write(b"%03d" % (train_list[i],))
            tf.write(UNIX_LINE_ENDING)

    with open(test_file, "wb") as tf:
        for i in range(len(test_list)):
            tf.write(b"%03d" % (test_list[i],))
            tf.write(UNIX_LINE_ENDING)


if __name__ == '__main__':
    random_data()
