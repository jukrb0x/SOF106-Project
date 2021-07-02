from tensorflow.keras import layers, models


# Convolutional Neural Network
class CNN:
    def __init__(self):
        model = models.Sequential()

        model.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(layers.AveragePooling2D((2, 2)))
        model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
        model.add(layers.AveragePooling2D((2, 2)))
        model.add(layers.Conv2D(filters=120, kernel_size=(3, 3), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(84, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))

        # Display the basic structure of the model
        model.summary()

        self.model = model
