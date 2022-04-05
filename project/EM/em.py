from numpy import append
from Utils.GaussianDistribution import GaussianDistribution
from Utils.Cluster import Cluster
class ExpectationMaximization:

    def __init__(self, samples, k) -> None:
        # the number of normal distributions to consider for assignment
        self.k = k
        # the space of samples
        # each sample is associated with an x value and an associated cluster
        self.space = samples

        # the distributions where the index of each distribution is the associated k
        self.distributions = list()
        # |clusters| = k

        clusters = list()

        # the guesses
        self.w = list()

        for dist_num in range(k):
            clusters.append(Cluster(list(), dist_num))

        # seperate each sample into the correct cluster
        for sample in samples:
            clusters[sample.getY()].append(sample)
        
        # create distributions
        for idx, cluster in enumerate(clusters):
            self.distributions.append(GaussianDistribution(cluster, len(samples), idx ) )


    def e_step(self):
        # seperating the ws
        seperated_w = list()
        # making new clusters
        new_clusters = list()
        for k in range(self.k):
            new_clusters.append(Cluster(list(), k))
            seperated_w.append(list())
        # guess each z^(i)

        # determine the w_j^(i) where j is the associated cluster and i is the point
        # for each point determine w_j then argmax that, we assign z^(i)

        for sample in self.samples:
            # calculate metric for the probability of each of the possible distributions
            w = list()
            # calculate the gaussian density sum
            density_sum = 0
            gdens = list()
            for idx, distribution in enumerate(self.distributions):
                gden = distribution.calculate_gaussian_density(sample)
                density_sum += gden * distribution.getPhi()
                gdens.append(gden)

            for idx, distribution in enumerate(self.distributions):
                p = ( gdens[idx] * distribution.getPhi() ) / density_sum

                w.append(p)

            # in the new clusters, add this sample to the associated cluster
            # with the biggest value
            biggest = max(w)
            new_y = w.index(biggest)
            sample.setY(new_y)
            new_clusters[new_y].addSample(sample)

            # add the w to the proper list
            seperated_w[new_y].append(biggest)

            # we may not even need this anymore as it is not being passed anymore
            self.w.append(w)

        # update dists with their new cluster and set of ws for each sample in the
        # cluster
        for idx, distribution in enumerate(self.distributions):
            distribution.replace_cluster(new_clusters[idx])
            distribution.replace_w(seperated_w[idx])
    
    def m_step(self):

        # update theta based on the e step 
        for distribution in self.distributions:
            distribution.calculate_phi()
            distribution.calculate_mu()
            distribution.calculate_big_sig()

        self.clear_w()

    def clear_w(self):
        self.w = list()