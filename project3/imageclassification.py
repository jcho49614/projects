import tensorflow as tf
import os
import cv2
import matplotlib
import imghdr

#check for image validity!
data_dir = 'data'
image_exts = ['jpeg', 'jpg', 'png']

for image_class in os.listdir(data_dir): #finds data_dir, which is 'data' and creates image_class -- dog or cat folder
    for image in os.listdir(os.path.join(data_dir, image_class)): #finds individual images in either 'dog' or 'cat', os.path.join gives directory
        image_path = os.path.join(data_dir, image_class, image) #path of the individual image.
        try: #try this. if not, go to exception.
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path) #imghdr depreciated...
            if tip not in image_exts: #img-exts secure form of image. 
                print('Image not in ext list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e: #logs down the error code in e.
            print('Issue with image {}: errorcode {}'.format(image_path, e))

import numpy as np
from matplotlib import pyplot as plt

data=tf.keras.utils.image_dataset_from_directory('data') #stores into files named data

data_iterator = data.as_numpy_iterator()
batch = data_iterator.next()
