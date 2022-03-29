from Utils.Sample import Sample
from matplotlib import image, pyplot
import os


def load_image_as_samples(image_name):
    cwd = os.getcwd()
    utils_path = cwd+"\\project\\Utils\\"
    # load image as pixel array
    img = image.imread(utils_path+image_name)
    samples = []
    for row in range(len(img)):
        for col in range(len(img[row])):
            rgb = img[row][col]
            sample = Sample(rgb, 0)
            samples.append(sample)
    return samples


