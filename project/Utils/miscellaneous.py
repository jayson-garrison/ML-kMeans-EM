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

def load_gaussian_file_as_samples(file_no, k, linux=False):
    cwd = os.getcwd()
    if not linux:
        local_path = cwd+"\\project\\Datasets\\Gaussian\\"
    else:
        local_path = cwd+"/project/Datasets/Gaussian/"
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
    
def visualize_gaussian_1d(file_no, estimted_means=[], save_path="", show=True, linux=False):
    cwd = os.getcwd()
    if not linux:
        local_path = cwd+"\\project\\Datasets\\Gaussian\\"
    else:
        local_path = cwd+"/project/Datasets/Gaussian/"
        
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


def load_iris_data_as_samples(k, linux=False):
    cwd = os.getcwd()
    if not linux:
        local_path = cwd+"\\project\\Datasets\\Iris\\"
    else:
        local_path = cwd+"/project/Datasets/Iris/"
    fname = local_path+"iris.csv"
    file = open(fname)
    samples = []
    for line in file:
        content = line.split(',')
        x = np.array([[float(content[0]), float(content[1]), float(content[2]), float(content[3])]])
        x = x.T
        y = content[4]
        sample = Sample(x, np.random.randint(k), y)
        samples.append(sample)
    return samples
        

def sum_squared_errors(samples, target):
    sse = 0
    for sample in samples:
        x = np.array(sample.getX())
        dif = target - x
        for dimension in dif:
            sse += dimension * dimension
    return sse


def silhouette(clusters, centroids):
    # a = mean intra-cluster distance
    a = 0
    tot = 0
    for idx in range(len(centroids)):
        samples = clusters[idx].getX()
        centroid = centroids[idx]
        tot += len(samples)
        a += sum_squared_errors(samples, centroid)
    a = a/tot

    # b = mean nearest-cluster distance
    b = 0
    for i in range(len(centroids)):
        samples = clusters[i].getX()
        for sample in samples:
            # Find the smallest nearest-cluster distance for the current sample
            distances = []
            for j in range(len(centroids)):
                if j == i: continue
                dif = centroids[j] - np.array(sample.getX())
                dist = 0
                for dimension in dif:
                    dist += dimension * dimension
                distances.append(dist)
            b += min(distances)
    b = b/tot

    # Now the silhouette idx is given by (b-a)/max(a,b)
    return (b-a)/max(a,b)


def dunn(clusters):
    # delta = the smallest distance between any two points not in the same cluster
    delta = float('inf')
    for i in range(len(clusters)):
        samples1 = clusters[i].getX()
        for j in range(len(clusters)):
            if j==i: continue
            samples2 = clusters[j].getX()
            # i and j are keeping track of the clusters being compared
            for s1 in samples1:
                for s2 in samples2:
                    dif = np.array(s1.getX()) - np.array(s2.getX())
                    dist = 0
                    for dimension in dif:
                        dist += dimension * dimension
                    if dist < delta:
                        delta = dist

    # Delta = the maximum distance between any two points in the same cluster
    Delta = 0
    for cluster in clusters:
        samples = cluster.getX()
        for i in range(len(samples)):
            for j in range(i, len(samples)):
                x1 = np.array(samples[i].getX())
                x2 = np.array(samples[j].getX())
                dif = x1 - x2
                dist = 0
                for dimension in dif:
                    dist += dimension * dimension
                if dist > Delta:
                    Delta = dist
    
    # The dunn index is measured by the ratio between (smallest nearest neighbor) and (largest cluster diameter)
    return delta/Delta


