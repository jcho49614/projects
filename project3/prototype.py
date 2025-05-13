import tensorflow as tf
import os

testing = 'data'
valid_exts = ['jpg', 'jpeg', 'png']
for image_class in os.path.join(testing):
    for image in os.path.join(testing, image_class):
        print(image)