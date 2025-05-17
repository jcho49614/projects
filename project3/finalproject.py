from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy
import cv2
import os
from tkinter import Tk, filedialog

model = load_model(os.path.join('finalmodel', 'catdogmodel.h5'))

print("Welcome to the Image Classifier!")
response = input("Do you want to proceed? (yes/no): ").strip().lower() #striplower is last word

if response not in ['yes', 'y']:
    print("Exiting program.")
    exit()


print("Please select an image file...")


Tk().withdraw() #main command prompt withdraw
file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

if not file_path:
    print("No file selected. Exiting.")
    exit()


img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
resize = tf.image.resize(img, (256, 256))
input_tensor = numpy.expand_dims(resize / 255.0, 0)


yhat = model.predict(input_tensor)[0][0]

print(f"\nPrediction confidence: {yhat:.4f}")
if yhat > 0.5:
    print("The image is classified as: DOG")
else:
    print("The image is classified as: CAT")