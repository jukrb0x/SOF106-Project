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

        # FIXME: remove me
        # try:
        #     with open("./img-2.png", "wb") as fh:
        #         # fh.write(base64.urlsafe_b64decode(self.img_base64_path))
        #         fh.write(img)
        # except:
        #     print("Exception with reading the image")

    def predict(self):
        x = self.img_array
        y = self.cnn.model.predict(x)
        prob = self.cnn.model.predict_proba(x)
        # print(self.img_base64_path)
        print(y[0])
        predict_digit = np.argmax(y[0])
        print('\tPredict digit: ', predict_digit)
        self.digit = predict_digit
        self.probability = prob
        print("PROB IS ", prob)

# debugging usage
# if __name__ == "__main__":
#     test_req = {
#         "imgValue": "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"
#     }
#
#     prediction = Predict(test_req['imgValue'])
#     # prediction = Predict("./5.png", is_base64=False)
#     prediction.base64_to_image()
#     prediction.predict()
#     try:
#         with open("./img-test.png", "wb") as fh:
#             fh.write(base64.urlsafe_b64decode(test_req['imgValue']))
#     except:
#         print("WTF!")
