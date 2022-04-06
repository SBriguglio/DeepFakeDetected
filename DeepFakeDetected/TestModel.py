import os
from pathlib import Path

import keras.preprocessing.image_dataset
import numpy as np
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
import keras.backend as k

from keras.models import Model, Sequential
from keras.losses import SparseCategoricalCrossentropy
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization, Rescaling
from keras.layers import Conv2D, SeparableConv2D, MaxPooling2D, LeakyReLU, Activation

os.system('color')
from termcolor import colored

seed = 1337
np.random.seed(seed)
tf.random.set_seed(seed)
image_path = "../DeepFakeDetected/resources/Processed/split"
train_path = image_path + "/train"
val_path = image_path + "/validate"
models_path = "../DeepFakeDetected/models"
df_path = image_path + "/deepfakes/"
or_path = image_path + "/originals/"
image_size = (512, 384)  # (512, 384)
batch_size = 32
# validation_split = 0.2 # Must be set manually below when data is manually split
epochs = 15


def test():
    training_set = keras.preprocessing.image_dataset.image_dataset_from_directory(train_path, batch_size=batch_size,
                                                                                  image_size=image_size,
                                                                                  validation_split=0.001,
                                                                                  subset="training", seed=seed)
    validation_set = keras.preprocessing.image_dataset.image_dataset_from_directory(val_path, batch_size=batch_size,
                                                                                    image_size=image_size,
                                                                                    validation_split=0.999,
                                                                                    subset="validation", seed=seed)

    num_classes = len(training_set.class_names)

    model = Sequential([
        Rescaling(1./255, input_shape=(image_size[0], image_size[1], 3)),
        Conv2D(16, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(num_classes)
    ])

    model.compile(optimizer='adam',
                  loss=SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    history = model.fit(
        training_set,
        validation_data=validation_set,
        epochs=epochs,
        shuffle=True,
        use_multiprocessing=True
    )

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    # prompts to save model
    # save(model)
    # or, just save model directly
    model_name = "UC_e50_(VAL_ACC_HERE)"
    m_path = models_path + "/" + model_name
    model.save(m_path)
    print(colored("Model has been saved: {}".format(m_path), "blue"))


def save(model):
    while 1:
        r = input(colored("Do you want to save this model? (y/n):\n", "green"))
        if r == 'y' or r == 'Y':
            break
        elif r == 'n' or r == "N":
            confirm = input(colored("Your model will be lost. Are you sure you don't want to save? (y/n):\n", "red"))
            if r == 'y' or r == 'Y':
                return

    print(colored("IMPORTANT: This step will overwrite other models with the same name. Choose a unique name.",
                  "yellow"))
    name = input(colored("Please enter a name for the model: ", "green"))
    m_path = models_path + "/" + name
    model.save(m_path)
    print(colored("Model has been saved: {}".format(m_path), "blue"))


if __name__ == '__main__':
    test()
