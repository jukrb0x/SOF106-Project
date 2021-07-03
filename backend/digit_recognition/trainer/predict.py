import os
import shutil
from io import BytesIO
import base64
from PIL import Image
import numpy as np
import tensorflow as tf
from .model import CNN

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
TRAINER_DIR = os.path.join(PROJECT_ROOT, 'trainer/')
CACHE_DIR = os.path.join(PROJECT_ROOT, 'cache/')


class Predict:
    def __init__(self, img_path: str = None, is_base64=True):
        self.is_base64 = is_base64
        self.img_path = img_path  # base64 encoded image
        self.img_array = ''  # nd-array from processed image
        self.digit = None  # predict digit
        self.probability = None  # predict probability
        self.mnist_image_size = (28, 28)
        # load the latest checkpoint
        checkpoint_dir = os.path.join(PROJECT_ROOT, 'checkpoint/')
        latest_checkpoint = tf.train.latest_checkpoint(checkpoint_dir)  # path defined in train.py
        self.cnn = CNN()
        # load network weights
        print("latest checkpoint: ", latest_checkpoint)
        self.cnn.model.load_weights(latest_checkpoint)

    def base64_to_image(self):
        # cache folder operation
        if os.path.exists(os.path.join(PROJECT_ROOT, 'cache')):
            for file_name in os.listdir(CACHE_DIR):
                file_path = os.path.join(CACHE_DIR, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'Failed to remove cache files {file_path}: {e}')
        else:
            os.mkdir(CACHE_DIR, 755)

        if self.is_base64:
            img = Image.open(BytesIO(base64.urlsafe_b64decode(self.img_path)))
        else:
            img = Image.open(self.img_path)
        img.save(os.path.join(PROJECT_ROOT, 'cache/original.png'))  # original image
        img = img.resize(self.mnist_image_size)
        img.save(os.path.join(PROJECT_ROOT, 'cache/resized.png'))  # resized image

        # the image passed from the frontend is transparent, add the white background
        # if this setup is done in the frontend then will improve the performance
        white_bg = Image.new('RGBA', self.mnist_image_size, (255, 255, 255))
        white_bg.paste(img, (0, 0, self.mnist_image_size[0], self.mnist_image_size[1]), img)
        img = white_bg.convert('L')
        img.save(os.path.join(PROJECT_ROOT, 'cache/grayscaled.png'))  # grayscaled image
        img = np.reshape(img, (28, 28, 1)) / 255  # make an reshaped array from img

        x = np.array([1 - img])  # get the coordinate of x

        # export to instance-self
        self.img_array = x

    def predict(self):
        x = self.img_array
        y = self.cnn.model.predict(x)
        print(y[0])
        predict_digit = np.argmax(y[0])
        print('\tPredict digit: ', predict_digit)
        self.digit = predict_digit
        # self.probability = None
