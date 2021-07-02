import os
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, utils, optimizers
from model import CNN


class DataSource:
    """
    handle the MNIST training data source
    """

    def __init__(self):
        mnist_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + '/MNIST/mnist.npz'
        print("MNIST dataset Local path: ", mnist_path)
        # load the dataset from the local path, which will be created if not exists.
        (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data(path=mnist_path)

        # Normalize data (scale them between 0 and 1 to improve training performance)
        train_images = utils.normalize(train_images, axis=1)
        test_images = utils.normalize(test_images, axis=1)

        # FIXME: what is this for?
        # reshape the image abaabaabaaba
        train_images = train_images.reshape((60000, 28, 28, 1)).astype('float') / 255
        test_images = test_images.reshape((10000, 28, 28, 1)).astype('float') / 255
        train_labels = utils.to_categorical(train_labels)
        test_labels = utils.to_categorical(test_labels)

        # export to instance-self
        self.train_images, self.test_images = train_images, test_images
        self.train_labels, self.test_labels = train_labels, test_labels


