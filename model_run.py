import pgn_to_custom_format
import numpy as np
import train_model
from importlib import reload
from tensorflow import keras
from importlib import reload
path_to_training_data=''

def define_path(path):
    global path_to_training_data 
    path_to_training_data = path

def model_run(move):
    evaluation_data = pgn_to_custom_format.read_pgn_files(path_to_training_data)
    game_data = np.asarray(evaluation_data, dtype=object)
    XTest = game_data[:,2]
    XTest = np.stack(XTest, axis=0)
    YTest = game_data[:,0]
    YTest = np.stack(YTest, axis=0)
    
    prediction = model.predict(XTest[move:move+1], verbose=0)
    
       
    return prediction,YTest[move]
    
model = keras.models.load_model('/home/matz/Documents/Git_software/Training_und_Modelle/2018_S5_relu_ab1')