import tensorflow as tf
import os
import cv2
import imghdr
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout

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


data = tf.keras.utils.image_dataset_from_directory('data') #categorizes into class
data = data.map(lambda x,y: (x/255, y)) #sizing data
data_iterator = data.as_numpy_iterator() #easier --> numpy for batches!

train_size = int(len(data) * .5)
val_size = int(len(data) * .25) + 1
test_size = int(len(data) * .25)
#data size allocation.

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size + val_size).take(val_size)
#allocation of data using take/skip

#building deep learning model

model = Sequential() #chronological order

#Conv2D: is a layer/filter. first number is amount of filters, second is size of filter, 3rd is stride.
#input_shape represents size, size, and colorway.

#MaxPooling2D(): is a way to condense data.

#Flatten(): Flattens 3D models to 1D
#Dense(): Creates neurons and connects.
#ReLU: max(0, x). Often used for image classificatoin
#Signoid: Used for binary classification. Ergo, if there are 2 options, use Signoid and BinaryCrossentropy
#Softmax: used for non-binary classification. More than 2 options, use Softmax and CategorialCrossentropy

model.add(Conv2D(16, (3,3), 1, activation = 'relu', input_shape=(256,256,3)))
model.add(MaxPooling2D()) #condenses by half
model.add(Conv2D(32, (3,3), 1, activation = 'relu'))
model.add(MaxPooling2D()) #condenses by half
model.add(Conv2D(16, (3,3), 1, activation = 'relu'))
model.add(MaxPooling2D()) #condenses by half

model.add(Flatten()) #flattens to single model
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

model.summary()


