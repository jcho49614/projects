import tensorflow as tf
import os
import cv2
import imghdr
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout # type: ignore
import numpy as np


testing = 'data'
valid_exts = ['jpg', 'jpeg', 'png']

for image_class in os.listdir(testing): # testing is data folder. list directory of testing and put in image class
    classdir = os.path.join(testing, image_class) 
    for image in os.listdir(classdir): #same thing above, but images now. Doesn't actually store the image only the directory.
        imagedir = os.path.join(classdir, image)
        image = cv2.imread(imagedir)
        extension = imghdr.what(imagedir)
        if extension not in valid_exts: #originally I used an try/except. Realized that it wasn't needed.
            print("Image {} is not valid!".format(imagedir))
        elif image is None: #cv2 returns "None" to unreadable images.
            print("Image {} is not valid!".format(imagedir))
        else:
            print("Image {} is valid! Using now.".format(imagedir)) 


data = tf.keras.utils.image_dataset_from_directory('data') #categorizes into class -- processes it.
data = data.map(lambda x,y: (x/255, y)) #sizing data and scaling it so it would be smaller
data_iterator = data.as_numpy_iterator() #puts the data into numpy form and allows us to use "batch".

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
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile('adam', loss=tf.losses.BinaryCrossentropy(), metrics=['accuracy'])

model.summary() #shows accurate summary of model.

#training the model.


logdir = 'logs' #saves everything in "logs"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir) #creates callbacks
hist = model.fit(train, epochs=1000, validation_data=val, callbacks=[tensorboard_callback])
#trains the model: uses train dataset, 20 times, uses validation data to validate, and callbacks on tensorboard_callback


from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy

pre = Precision()
re = Recall()
acc = BinaryAccuracy()

for batch in test.as_numpy_iterator(): #model.predict requires batch[0].
    #y is used for identification.
    x, y = batch
    yhat = model.predict(x)
    pre.update_state(y, yhat)
    re.update_state(y, yhat)
    acc.update_state(y,yhat)

print(pre.result(), re.result(), acc.result())

#gpt, img is the image I want to have it input. help me!

from tensorflow.keras.models import load_model
model.save(os.path.join('finalmodel', 'catdogmodel.h5'))
