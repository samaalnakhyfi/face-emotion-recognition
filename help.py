from tensorflow.keras.models import Sequential, model_from_json
import tensorflow_hub as hub
from tensorflow.keras.optimizers import Adam
import cv2
import matplotlib.pylab as plt
import numpy as np
import joblib
from tkinter import *
from keras.models import Sequential
from keras import layers
from keras.layers import Input,Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation,GlobalMaxPooling2D,GlobalAveragePooling2D,BatchNormalization
from keras import applications
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.applications.efficientnet import EfficientNetB3
def create_model():
    input_shape = (48, 48, 1)

    # Input layer
    inputs = Input(shape=input_shape)

    # 1st CNN layer
    x = Conv2D(64, (3, 3), padding='same')(inputs)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.25)(x)

    # 2nd CNN layer
    x = Conv2D(128, (5, 5), padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.25)(x)

    # 3rd CNN layer
    x = Conv2D(512, (3, 3), padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.25)(x)

    # 4th CNN layer
    x = Conv2D(512, (3, 3), padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Dropout(0.25)(x)

    # Flattening layer
    x = Flatten()(x)

    # Fully connected 1st layer
    x = Dense(256)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.25)(x)

    # Fully connected 2nd layer
    x = Dense(512)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.25)(x)

    # Output layer (7 classes)
    outputs = Dense(7, activation='softmax')(x)

    # Define the model
    model = Model(inputs=inputs, outputs=outputs)

    return model

def load_model():
    model = create_model()
    model.load_weights("model.h5")
    print("Loaded model from disk")
   
    return model

model=load_model()

def predict_image(image_path):
    le=joblib.load('labels')
    #model=load_model()
    image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    image_resized = cv2.resize(image, (48, 48))
    plt.imshow(image_resized, cmap='gray')
    x = np.expand_dims(np.array(image_resized), axis=-1)
    x = np.expand_dims(x, axis=0)
    res = model.predict(x)
    return le.classes_[np.argmax(res)]

    


