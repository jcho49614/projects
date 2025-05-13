import tensorflow as tf
import os
import cv2
import imghdr

testing = 'data'
valid_exts = ['jpg', 'jpeg', 'png']

for image_class in os.listdir(testing):
    classdir = os.path.join(testing, image_class)
    for image in os.listdir(classdir):
        imagedir = os.path.join(classdir, image)
        image = cv2.imread(imagedir)
        extension = imghdr.what(imagedir)
        if extension not in valid_exts:
            print("Image {} is not valid!", format(imagedir))
        elif image is None:
            print("Image {} is not valid!", format(imagedir))
        else:
            print("Image {} is valid! Using now.".format(imagedir)) 


