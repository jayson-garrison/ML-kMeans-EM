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
            clusters[sample.getY()].addSample(sample)
        
        # create distributions
        for idx, cluster in enumerate(clusters):
            self.distributions.append(GaussianDistribution(cluster, len(samples), idx, samples[0].getDim() ) )

    def learn(self, convergence):
        i = 0
        while i < convergence:
            print(f'number of iter: {i}')
            for idx, distribution in enumerate(self.distributions):
                print(f'dist number: {idx}')
                print(f'phi:{distribution.getPhi()} mu: {distribution.getMu()} cov: {distribution.getBigSig()}')
                print(f'w length: {len(distribution.getW())}')
                print('---------------------------------------------------------------------')
            self.e_step()
            self.m_step()
            i += 1

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

        for sample in self.space:
            # calculate metric for the probability of each of the possible distributions
            w = list()
            # calculate the gaussian density sum
            density_sum = 0
            gdens = list()

            if True:
                # determine the density for each dist of this point
                for distribution in self.distributions:
                    gdens.append(distribution.calculate_gaussian_density(sample.getX()))
                # for i in range(len(self.distributions)):
                #     distribution = self.distributions[i]
                #     gdens.append(distribution.calculate_gaussian_density(sample.getX()))

                # the one with the highest density is the best dist to 
                # assign this point to
                #print(gdens)
                biggest = max(gdens)
                new_y = gdens.index(biggest)
                sample.setY(new_y)
                new_clusters[new_y].addSample(sample)

            else:
            
                for idx, distribution in enumerate(self.distributions):
                    gden = distribution.calculate_gaussian_density(sample.getX())
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

            #print(len(seperated_w))
            #print(seperated_w)
            #print(seperated_w)
            # update dists with their new cluster and set of ws for each sample in the
            # cluster
        for idx, distribution in enumerate(self.distributions):
            distribution.replace_cluster(new_clusters[idx])
            #print(seperated_w[idx])
            distribution.replace_w(seperated_w[idx])
            #print('replaced w')

    def m_step(self):

        # update theta based on the e step 
        for distribution in self.distributions:
            distribution.calculate_phi()
            distribution.calculate_mu()
            distribution.calculate_big_sig()

        self.clear_w()

    def getMeans(self):
        means = list()

        for distribution in self.distributions:
            means.append(distribution.getMu())

        return means
    def clear_w(self):
        self.w = list()

    def getDistributions(self):
        return self.distributions

    def evaluate_likelihood(self):
        # the likelihood that two points chosen to be in the same cluster by a clustering algorithm
        # was generated by the same source distribution, i.e., the fraction of pairs belonging to same output
        # cluster that were generated from the same source.
        N = len(self.space)
        likelihood = 0
        for distribution in self.distributions:
            # Each cluster may contain points from more than one class.
            # Determine the number of points from each class in the cluster.
            true_label_cts = dict()
            n = len(distribution.getCluster().getX())
            for sample in distribution.getCluster().getX():
                label = sample.getTrueLabel()
                if label not in true_label_cts:
                    true_label_cts[label] = 0
                true_label_cts[label] += 1
            num_matching_pairs = 0
            # The number of pairs in the current output (cluster) that were generated from the same source
            # is the sum of the handshake number for each of the class counts for the cluster
            for ct in true_label_cts:
                num_matching_pairs += (ct)*(ct-1)/2
            likelihood += num_matching_pairs/(n-1)
        # We have summed the fraction of pairs belonging to the same output (for each output)
        # Now we divide by the total number of points
        likelihood = likelihood/N
        return likelihood