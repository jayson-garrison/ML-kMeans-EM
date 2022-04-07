from cmath import pi
import numpy as np
from Utils.Cluster import Cluster
class GaussianDistribution:

    def __init__(self, cluster, num_samples, k) -> None:
        '''
        Gaussian Distribution

        phi := the proportion of this distribution related to the whole sample space of points

        mu := the mean

        big_sig := the covariance

        @param points: the points in the distribution

        @param num_samples: the number of samples in the whole space (where points are a subset
        of this space)
        
        '''
        self.num_samples = num_samples
        self.id = k
        # if div doesnt work use matmul by a scalar
        self.dim = cluster.getX()[0].getDim()
        self.cluster = cluster
        self.phi = cluster.getMagnitude() / num_samples
        self.w = list()

        total = np.zeros(self.dim)

        for point in cluster.getX():
            total += point.getX()
        
        self.mu = total / self.cluster.getMagnitude()
        
        cov = np.zeros((self.dim, self.dim))

        for point in cluster.getX():
            # verify this
            # var = np.divide(np.matmul(np.subtract(point.getX(), self.mu), np.matrix.transpose(np.subtract(point.getX(), self.mu))), self.cluster.getMagnitude())
            # cov = np.add(var, cov)
            cov += np.matmul((point.getX() - self.mu), np.transpose(point.getX() - self.mu))
            
        self.big_sig = cov / cluster.getMagnitude()
        # print(self.big_sig)
        # exit()

    def calculate_gaussian_density(self, given_sample):
        gd = 1 / ( (2*np.pi)**(self.dim/2) * (np.linalg.det(self.big_sig))**(.5) )
        gd = gd * np.exp( -.5 * np.matrix.transpose( given_sample - self.mu ) * \
                           np.linalg.pinv(self.big_sig) * (given_sample - self.mu) )

        return gd

    def calculate_phi(self, ng=False):
        '''
        calculate the phi based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''
        if ng:
            #perform the calculation for phi based on the m step
            # self.points = points
            self.phi = 0
            # exit()
            for possibility in self.w:
                self.phi += possibility

            self.cum_w = self.phi

            if len(self.w) != 0:
                self.phi = self.phi / len(self.w)
        # intuitive
        else:
            self.phi = self.cluster.getMagnitude() / self.num_samples

    def calculate_mu(self, ng=False):
        '''
        calculate the mu based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''

        if ng:
            # perform the calculate for mu based on the m step
            # reset mu for update
            self.mu = np.zeros(self.dim)

            for idx, possibility in enumerate(self.w):
                #print(possibility)
                #print(self.cluster.getX()[idx].getX())
                self.mu += possibility[0] * self.cluster.getX()[idx].getX()

            self.mu = self.mu / self.cum_w

        # intuitive
        else:
            self.mu = np.zeros(self.dim)

            for sample in self.cluster.getX():
                self.mu += sample.getX()
            
            self.mu = self.mu / self.cluster.getMagnitude()

    def calculate_big_sig(self, ng=False):
        '''
        calculate the big_sig based on the EM update (Ng)

        @param points: the new points associated with the distribution
        '''

        if ng:
            # perform the calculation for big sig based on the m step
            # reset big sig for update
            self.big_sig = np.zeros((self.dim, self.dim))

            for idx, possibility in enumerate(self.w):
                self.big_sig += possibility * np.matmul( (self.cluster.getX()[idx].getX() - self.mu), \
                                np.transpose(self.cluster.getX()[idx].getX() - self.mu) )

            self.big_sig = self.big_sig / self.cum_w
        
        # intuitive
        else:

            cov = np.zeros((self.dim, self.dim))

            for point in self.cluster.getX():
                # verify this
                # var = np.divide(np.matmul(np.subtract(point.getX(), self.mu), np.matrix.transpose(np.subtract(point.getX(), self.mu))), self.cluster.getMagnitude())
                # cov = np.add(var, cov)
                cov += np.matmul((point.getX() - self.mu), np.transpose(point.getX() - self.mu))
            
        self.big_sig = cov / self.cluster.getMagnitude()

    def replace_cluster(self, new_cluster):
        self.cluster = new_cluster

    def replace_w(self, new_w):
        self.w = new_w

    def addW(self, a_w):
        self.w.append(a_w)

    def getPhi(self):
        '''
        @returns the phi of the distribution
        '''
        return self.phi

    def getMu(self):
        '''
        @returns the mu of the distribution
        '''
        return self.mu

    def getBigSig(self):
        '''
        @returns the big_sig of the distribution
        '''
        return self.big_sig

    def getW(self):
        return self.w