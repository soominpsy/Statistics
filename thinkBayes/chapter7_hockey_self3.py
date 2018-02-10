import thinkbayes
import thinkplot
import math
import numpy
import scipy

class Hockey(thinkbayes.Suite):
    def __init__(self):
        pmf = MakeGaussianPmf(mu = 2.7, sigma = 0.3, nsigma = 4)			# MakeGaussianPmf
        thinkbayes.Suite.__init__(self, pmf)

    def Likelihood(self, data, hypo):
        lam = hypo
        k = data
        like = EvalPoissonPmf(lam, k)    				# EvalPoissonPmf
        return like



    def UpdateSet(self, dataset):
        for data in dataset:
            for hypo in self.Values():
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
        self.Normalize()




def MakeGaussianPmf(mu, sigma, nsigma, n = 101):
    pmf = thinkbayes.Pmf()
    low = mu - sigma * nsigma
    high = mu + sigma * nsigma

    for x in numpy.linspace(low, high, n):
        p = EvalGaussianPdf(x, mu, sigma)			# EvalGaussianPdf
        pmf.Set(x,p)
    pmf.Normalize()
    return pmf

def EvalGaussianPdf(x, mu, sigma):
    return scipy.stats.norm.pdf(x, mu, sigma)
def EvalPoissonPmf(lam, k):
    return (lam)**k * math.exp(-lam)/ math.factorial(k)


def main():
    p1 = Hockey()
    p2 = Hockey()
    p1.UpdateSet([0,2,8,4])
    p2.UpdateSet([1,3,1,0])

    thinkplot.Clf()
    thinkplot.preplot(num=2)
    thinkplot.Pmf(p1)
    thinkplot.Pmf(p2)
    thinkplot.Save(root='hockey_self3',xlabel='',ylabel='Probability',formats=['pdf'])


if __name__=="__main__":
    main()




