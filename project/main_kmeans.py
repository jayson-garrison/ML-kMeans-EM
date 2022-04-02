from Utils.miscellaneous import load_image_as_samples, load_gaussian_file_as_samples, visualize_gaussian_1d
from KMeans.kmeans import KMeans
import numpy as np
from matplotlib import pyplot

if  __name__ == "__main__":
    k = 3
    # samples = load_image_as_samples("Colors.jpg", k)
    samples = load_gaussian_file_as_samples(2, k)
    model = KMeans(samples=samples, k=k, dimensions=1)
    model.learn(C=2/len(samples))
    llhd = model.evaluate_likelihood()
    print(llhd)
    visualize_gaussian_1d(file_no=2, estimted_means=model.getCentroids())
    
    # model.paint_by_numbers("TheLastSupper.jpg")
