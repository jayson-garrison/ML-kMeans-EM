from Utils.Cluster import Cluster
from Utils.Sample import Sample
import numpy as np
from matplotlib import image, pyplot
import numpy as np
import os

class KMeans():
    def __init__(self, samples, k, dimensions):
        self.samples = samples
        self.k = k
        self.dimensions = dimensions
        self.centroids = [] # there should be k p-dimensional mean vectors
        self.clusters = []

    def learn(self):
        self.initialize_clusters_and_centroids()
        num_changed_samples = len(self.samples)
        while(num_changed_samples > (len(self.samples)/10)):
            print("Re-Clustering")
            for k in range(self.k):
                centroid = self.compute_centroid(self.clusters[k])
                self.centroids[k] = centroid
            changed_samples = self.assign_points_to_clusters()
            num_changed_samples = len(changed_samples)
            self.print()

    def initialize_clusters_and_centroids(self):
        for k in range(self.k):
            self.clusters.append(Cluster(list(), k))
        for sample in self.samples:
            k = sample.getY()
            self.clusters[k].addSample(sample)
        for k in range(self.k):
            centroid = self.compute_centroid(self.clusters[k])
            self.centroids.append(centroid)

    def compute_centroid(self, cluster):
        centroid = np.zeros(self.dimensions)
        count = 0 # to avoid divide by zero
        for sample in cluster.getX():
            centroid += sample.getX()
            count += 1
        if count == 0: count = 1 # avoid divide by zero
        centroid = centroid/count
        return centroid
        
    def assign_points_to_clusters(self):
        changed_samples = list()
        for k in range(self.k):
            self.clusters[k].clear()
        for sample in self.samples:
            closest_k = 0
            closest_distance = float('inf')
            for k in range(self.k):
                dist = self.distance(sample.getX(), self.centroids[k])
                if dist<closest_distance:
                    closest_distance = dist
                    closest_k = k
            if sample.getY() != closest_k:
                changed_samples.append(sample)
                sample.setY(closest_k)
            self.clusters[closest_k].addSample(sample)
        return changed_samples

    def distance(self, point, target):
        dif = point-target
        for idx in range(len(dif)):
            dif[idx] = dif[idx]*dif[idx]
        return sum(dif)

    def print(self):
        print(self.centroids)

    def setCentroids(self, centroids):
        self.centroids = centroids
        
    def paint_by_numbers(self, image_name):
        cwd = os.getcwd()
        utils_path = cwd+"\\project\\Utils\\"
        # load image as pixel array
        img = image.imread(utils_path+image_name)
        for row in range(len(img)):
            for col in range(len(img[row])):
                pixel = img[row][col]
                closest_k = 0
                closest_distance = float('inf')
                for k in range(self.k):
                    dist = self.distance(pixel, self.centroids[k])
                    if dist<closest_distance:
                        closest_distance = dist
                        closest_k = k
                img[row][col] = self.centroids[closest_k]
        pyplot.imshow(img)
        pyplot.show()
