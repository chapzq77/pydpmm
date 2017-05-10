from __future__ import division
import numpy as np
from numpy.random import random

#fix var = 1
class UnivariateGaussian(object):


    def __init__(self,mu=None):
        self.mu = mu

    def rvs(self, size=None):
        return np.random.normal(self.mu,1,size)

    def set_mu(self,mu=None):
        self.mu = mu


    def sample_new_mu(self,x):
        return np.random.normal(0.5*x, 0.5, 1)

    def log_likelihood(self,x):
        x = np.reshape(x, (-1, 1))
        return (-0.5 * (x - self.mu) ** 2 - np.log(2 * np.pi )).ravel()


