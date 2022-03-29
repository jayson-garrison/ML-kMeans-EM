from Utils import Cluster, Sample
import numpy as np

class KMeans():
    def __init__(self, samples, k, dimensions):
        self.samples = samples
        self.k = k
        self.centroids = [] # there should be k p-dimensional mean vectors
        self.clusters = []

    def learn(self):
        self.initialize_clusters_and_centroids()
        some_point_changed = True
        while(some_point_changed):
            for k in range(self.k):
                centroid = self.compute_centroid(self.clusters[k])
                self.centroids[k] = centroid
            some_point_changed = self.assign_points_to_clusters()

    def initialize_clusters_and_centroids(self):
        for k in range(self.k):
            self.clusters.append(Cluster(list(), k))
        for sample in self.samples:
            k = sample.getY()
            self.clusters[k].addSample(sample)
        for k in range(self.k):
            self.compute_centroid(self.clusters[k])

    def compute_centroid(self, cluster):
        centroid = np.zeros(self.dimensions)
        count = 0
        for sample in cluster.getX():
            centroid += sample.getX()
            count += 1
        centroid = centroid/count
        return centroid
        
    def assign_points_to_clusters(self):
        some_point_changed = False
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
                some_point_changed = True
                sample.setY(k)
            self.clusters[k].addSample(sample)
        return some_point_changed

    def distance(self, point, target):
        dif = point-target
        for idx in range(len(dif)):
            dif[idx] = dif[idx]*dif[idx]
        return sum(dif)
        
    def paint_by_numbers(self, data):
        # for each point, assign it the value of the nearest mean vector
        pass
