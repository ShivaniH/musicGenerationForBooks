import tensorflow as tf
from keras.callbacks import ModelCheckpoint, LambdaCallback
from keras.callbacks import EarlyStopping, TensorBoard
import argparse
import midi
import os
import psutil

from constants import *
from dataset import *
from generate import *
from midi_util import midi_encode
from model import *

def main():
    models = build_or_load()
    train(models)

def train(models):
    print('Loading data')
    train_data, train_labels = load_all(styles, BATCH_SIZE, SEQ_LEN)

    cbs = [
         ModelCheckpoint(MODEL_FILE, monitor='loss', save_best_only=True, save_weights_only=True),
         EarlyStopping(monitor='loss', patience=5),
         TensorBoard(log_dir='out/logs', histogram_freq=1)
    ]

    print('Training')
    # train_data = np.array (train_data) 
    # train_labels = np.array (train_labels) 
    # print (train_labels[0].shape)
    # print ( train_data[0].shape ) 
    # print ( len(train_data) , len(train_data[0]), len(train_data[0][0]) , " data ",len(train_labels[0]), models[0]) 
    print (psutil.virtual_memory())
    models[0].fit(train_data, train_labels, callbacks=cbs, epochs=1000,  batch_size=BATCH_SIZE)
 

if __name__ == '__main__':
    main()
