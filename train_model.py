import numpy as np
from tensorflow import keras
from keras import layers

def train(XTrain, YTrain):
    input_shape = (12*64)

    model = keras.Sequential(
        [
            keras.Input(shape=input_shape),
            layers.Dense(192, activation="sigmoid"),
            layers.Dense(48, activation="sigmoid"),
            layers.Dense(12, activation="sigmoid"),
            #layers.Dense(768, activation="relu"),
            #layers.Dense(768, activation="relu"),
            #layers.Dense(768, activation="relu"),
            #layers.Dense(768, activation="relu"),
            layers.Dense(3, activation="softmax")
        ]
    )
    model.compile(loss='mean_squared_error',
                  optimizer='adam', metrics=['accuracy'])
    model.fit(XTrain, YTrain, epochs=10, verbose=True)

    return model

def evaluate(model, XTest, YTest):
    score = model.evaluate(XTest, YTest, verbose=True)

    print('Test score:', score[0])
    print('Test accuracy:', score[1])
    np.set_printoptions(threshold=np.inf, precision=2, suppress=True)

def predict(model, XTest, YTest):
    pass
    # print(model.predict(XTrain))
