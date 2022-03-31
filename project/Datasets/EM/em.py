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

        clusters = list(Cluster())

        # seperate each sample into the correct cluster
        for sample in samples:
            clusters[sample.getY()].append(sample)
        
        # create distributions
        for cluster in clusters:
            self.distributions.append(GaussianDistribution(cluster, len(samples) ) )


    def e_step(self):
        # guess each z^(i)

        # determine the w_j^(i) where j is the associated cluster and i is the point
        # for each point determine w_j then argmax that, we assign z^(i)

        for sample in self.samples:

        pass
    
    def m_step():
        # update theta based on the e step 
        pass