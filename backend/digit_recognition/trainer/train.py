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


class Train:
    """
    Training process
    """

    def __init__(self):
        self.cnn = CNN()
        self.data = DataSource()

    def train(self):
        # training batch size
        batch_size = 128
        # checkpoint save path
        checkpoint_path = "../checkpoint/training-cp{epoch:04d}.ckpt"
        checkpoint_dir = os.path.dirname(checkpoint_path)
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path,
            save_weights_only=True,
            verbose=1,
            save_best_only=True
        )
        #
        if tf.train.get_checkpoint_state(checkpoint_dir) is not None:
            print("The checkpoint is found, which will be rewritten!")
        # compile model
        self.cnn.model.compile(
            optimizer=optimizers.RMSprop(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        # start training
        self.cnn.model.fit(
            self.data.train_images,
            self.data.train_labels,
            epochs=50,
            batch_size=batch_size,
            callbacks=[checkpoint_callback],
            validation_data=(self.data.test_images, self.data.test_labels),
            verbose=2
        )

        # evaluate test
        test_loss, test_accuracy = self.cnn.model.evaluate(
            self.data.test_images, self.data.test_labels
        )

        # print eval test result
        print("Test loss: ", test_loss,
              "\t Test accuracy: ", test_accuracy)

        # save the entire model
        self.cnn.model.save('../saved_model/best')


if __name__ == '__main__':
    app = Train()
    app.train()
