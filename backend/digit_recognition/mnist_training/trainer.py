import os.path

from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow.keras import models, layers, utils
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.datasets import mnist

# checkpoint save path
checkpoint_path = "./model/training-cp{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Load dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
"""
(train_images, train_labels) = (x, y)
The image data plot the x-axis, and the result numbers plot the y-axis
"""
# Normalize data (scale them between 0 and 1 to improve training performance)
train_images = utils.normalize(train_images, axis=1)
test_images = utils.normalize(test_images, axis=1)


# Construct LaNet Network
# FIXME: need explanation here ?
# FIXME: LaNet ?
def create_model():
    model = models.Sequential()
    model.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.AveragePooling2D((2, 2)))
    model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    model.add(layers.AveragePooling2D((2, 2)))
    model.add(layers.Conv2D(filters=120, kernel_size=(3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(84, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    return model


# Initiate the model and save to path
model = create_model()
if tf.train.get_checkpoint_state is not None:
    latest_checkpoint = tf.train.latest_checkpoint(checkpoint_dir)
    print("The latest checkpoint path: ", latest_checkpoint)
    model.load_weights(latest_checkpoint)
else:
    model.save_weights(checkpoint_path.format(epoch=0))

batch_size = 128

# saver callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    save_freq=5 * batch_size)  # save every 5 epochs

# Display the basic structure of the model
model.summary()

# Compile the model
model.compile(
    optimizer=RMSprop(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy'])

# FIXME: What is this for?
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 训练网络，用fit函数, epochs表示训练个回合， batch_size表示每次训练多大的数据
# Train the model
model.fit(train_images,
          train_labels,
          epochs=50,
          batch_size=batch_size,
          callbacks=[cp_callback],
          validation_data=(test_images, test_labels),
          verbose=2)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("Test loss:", test_loss, "\tTest accuracy:", test_accuracy)

model.save('saved_model/best')
