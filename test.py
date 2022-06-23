from os import listdir
import cv2
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import random
from keras.models import  load_model
import sys

cap = cv2.VideoCapture(0)

# Dinh nghia class
class_name = ['Gau', 'Heo rung', 'Voi', 'Cao', 'Khi dot', 'Ha ma', 'Linh cau', 'Bao',
 'Su tu', 'Bo', 'Tuan loc', 'Te giac', 'Cuu', 'Ho', 'Ngua van']
# ['Bear', 'Boar' ,'Elephant' ,'Fox' ,'Gorilla', 'Hippopotamus' ,'Hyena', 'Leopard',
#  'Lion' ,'Ox', 'Reindeer', 'Rhinoceros' ,'Sheep' ,'Tiger' ,'Zebra']



# Load weights model da train
my_model = load_model('ANIMAL.h5')
my_model.load_weights("wieghts-test-CNN.hdf5")

while(True):
    # Capture frame-by-frame
    #

    ret, image_org = cap.read()
    if not ret:
        continue
    image_org = cv2.resize(image_org, dsize=None,fx=0.5,fy=0.5)
    # Resize
    image = image_org.copy()
    image = cv2.resize(image, dsize=(128, 128))
    image = image.astype('float')*1./255
    # Convert to tensor
    image = np.expand_dims(image, axis=0)

    # Predict
    predict = my_model.predict(image)
    # print("This picture is: ", class_name[np.argmax(predict[0])], (predict[0]))
    print(np.max(predict[0],axis=0))
    if (np.max(predict)>=0.8): #and (np.argmax(predict[0])!=0):


        # Show image
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1.5
        color = (0, 255, 0)
        thickness = 2

        cv2.putText(image_org, class_name[np.argmax(predict)], org, font,
                    fontScale, color, thickness, cv2.LINE_AA)

    cv2.imshow("Picture", image_org)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


