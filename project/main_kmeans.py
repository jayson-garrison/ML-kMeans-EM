from Utils.miscellaneous import load_image_as_samples
from KMeans.kmeans import KMeans
import numpy as np
from matplotlib import pyplot

if  __name__ == "__main__":
    k = 10
    samples = load_image_as_samples("TheLastSupper.jpg", k)
    model = KMeans(samples, k, 3)
    model.learn()
    # model.print()
    # centroids = [
    #     np.array([141.27525708,  83.04562434,  51.87597062]),
    #     np.array([71.20391167, 44.68660358, 35.25863302]),
    #     np.array([15.73987535,  9.83868618,  8.91354649]),
    #     np.array([174.26830247, 118.22713224,  81.88163265]),
    #     np.array([221.94372481, 125.39717818,  78.69422198])
    # ]
    # model.setCentroids(centroids)
    # model.print()
    model.paint_by_numbers("TheLastSupper.jpg")
    