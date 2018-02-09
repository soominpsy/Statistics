import scipy
import thinkbayes
from thinkbayes import Pdf

class Gaussian(Pdf):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
    def Density(self,x):
        return scipy.stats.norm.pdf(x, self.mu, self.sigma)

def main():
    gauss = Gaussian(0,1)


if __name__=="__main__":
    main()

