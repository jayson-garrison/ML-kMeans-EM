from Utils.Sample import Sample
from matplotlib import image, pyplot, lines
import numpy as np
import os


def load_image_as_samples(image_name, k):
    cwd = os.getcwd()
    jpg_path = cwd+"\\project\\Datasets\\JPGs\\"
    # load image as pixel array
    img = image.imread(jpg_path+image_name)
    samples = []
    for row in range(len(img)):
        for col in range(len(img[row])):
            rgb = img[row][col]
            sample = Sample(rgb, np.random.randint(k))
            samples.append(sample)
    return samples

def load_gaussian_file_as_samples(file_no, k):
    cwd = os.getcwd()
    local_path = cwd+"\\project\\Datasets\\Gaussian\\"
    fname = local_path+"File"+str(file_no)+".txt"
    file = open(fname)
    samples = []
    for line in file:
        content = line.split()
        if content[0] == "Gaussian":
            continue
        sample = Sample(np.array([float(content[1])]), np.random.randint(k), float(content[0]))
        samples.append(sample)
    return samples
    
def visualize_gaussian_1d(file_no, estimted_means=[], save_path="", show=True):
    cwd = os.getcwd()
    local_path = cwd+"\\project\\Datasets\\Gaussian\\"
    fname = local_path+"File"+str(file_no)+".txt"
    file = open(fname)
    X=dict()
    for line in file:
        content = line.split()
        # Skip header lines
        if content[0] == "Gaussian":
            continue
        # For non-header lines, store the generated point
        if float(content[0]) not in X:
            X[float(content[0])] = []
        X[float(content[0])].append(float(content[1]))    
    # Plot the generated points by distribution
    offset = 0
    idx = 0
    for key in X:
        pyplot.scatter(X[key], np.zeros(len(X[key]))+offset, alpha=.1)
        pyplot.scatter(key, offset, color='black', marker='d')
        offset += .01
    # Draw the estimated lines
    for x in estimted_means:
        pyplot.axvline(x=x, color='gray')

    # Add a legend
    black_diamond = lines.Line2D([], [], color='black', marker='d', linestyle='None', label='True Mean')
    gray_line = lines.Line2D([], [], color='gray', marker='_', linestyle='None', label='Estimated Mean')
    pyplot.legend(handles=[black_diamond, gray_line])
    # Remove the y-axis
    ax = pyplot.gca()
    ax.axes.get_yaxis().set_visible(False)
    # Rescale the figure
    fig = pyplot.gcf()
    fig.set_size_inches(8, 2)
    if show:
        pyplot.show()
    if save_path != "":
        pyplot.savefig(save_path)
    pyplot.close()


        



