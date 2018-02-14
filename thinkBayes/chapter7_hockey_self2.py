import numpy
import scipy
import thinkbayes
import thinkplot
from thinkbayes import Pmf
import math

class Hockey(thinkbayes.Suite):

    def __init__(self):
#        pmf = thinkbayes.MakeGaussianPmf(mu=2.7, sigma=0.3, num_sigmas=4)
        pmf = MakeGaussianPmf(mu=2.7, sigma=0.3, num_sigmas=4)
        thinkbayes.Suite.__init__(self, pmf)

    def Likelihood(self, data, hypo):
        lam = hypo
        k = data
        like = EvalPoissonPmf(lam, k)
        return like

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def UpdateSet(self, dataset):
        for data in dataset:
            for hypo in self.Values():
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
        self.Normalize()



def MakeGaussianPmf(mu, sigma, num_sigmas, n =101):
    pmf = thinkbayes.Pmf()
    low = mu - sigma * num_sigmas
    high = mu + sigma * num_sigmas
    
    for x in numpy.linspace(low, high, n):
        p = scipy.stats.norm.pdf(x, mu, sigma)     # this seems to return poisson distribution may du to iteration... 
#        p = EvalGaussianPdf(x, mu, sigma)
        pmf.Set(x, p)
    pmf.Normalize()
    return pmf

def EvalGaussianPdf(x, mu, sigma):
    return scipy.stats.norm.pdf(x, mu, sigma)
def EvalPoissonPmf(lam, k):
    return (lam)**k * math.exp(-lam) / math.factorial(k)
def EvalExpoentialPdf(lam, x):
    return lam * math.exp( -lam * x)





def main():
    print "1"
    hockey1 = Hockey()
#    print(type(hockey1))

    thinkplot.PrePlot(1)
    thinkplot.Pmf(hockey1) 
    thinkplot.Save(root='hockey_self2_prior',xlabel='',ylabel='Probability',formats=['pdf'])   
    
    print(hockey1.Values())
    for hypo in hockey1.Values():
        print(hockey1.Likelihood(2,hypo))

    hockey1.UpdateSet([0,2,4,3,8])
    thinkplot.Pmf(hockey1)
    thinkplot.Save(root='hockey_self2_posterior',xlabel='',ylabel='Probability',formats=['pdf'])


    print("No error, everything worked fine")

if __name__=="__main__":
    main()
