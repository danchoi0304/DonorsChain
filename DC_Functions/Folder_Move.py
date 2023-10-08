import shutil
import os

def move_to_outputs(filename):

    src = "C:\\Users\\danch\\OneDrive\\바탕 화면\\DonorsChain"
    dst = "C:\\Users\\danch\\OneDrive\\바탕 화면\\DonorsChain\\outputs"

    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))