from Utils.Sample import Sample
from matplotlib import image
import numpy as np
import os


def load_image_as_samples(image_name, k):
    cwd = os.getcwd()
    utils_path = cwd+"\\project\\Utils\\"
    # load image as pixel array
    img = image.imread(utils_path+image_name)
    samples = []
    for row in range(len(img)):
        for col in range(len(img[row])):
            rgb = img[row][col]
            sample = Sample(rgb, np.random.randint(k))
            samples.append(sample)
    return samples


