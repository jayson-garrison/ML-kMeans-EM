class KMeans_WMD():
    def __init__(self, documents, k, dims):
        self.documents = documents
        self.k = k
        self.dimensions = dims
        self.centroids = []
        self.clusters = []