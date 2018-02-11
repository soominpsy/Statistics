import thinkbayes
import thinkplot
import math
import numpy
import scipy

class Hockey(thinkbayes.Suite):
    def __init__(self):
        pmf = MakeGaussianPmf(mu = 2.8, sigma = 0.3, nsigma=4)   # MakeGaussianPmf
        thinkbayes.Suite.__init__(self, pmf)

    def Likelihood(self, data, hypo):
        lam = hypo
        k = data
        like = EvalPoissonPmf(lam, k)                            # EvalPoissonPmf
        return like

    def UpdateSet(self, dataset):
        for data in dataset:
            for hypo in self.Values():
                like = self.Likelihood(data, hypo) * hypo
                self.Set(hypo, like)
        self.Normalize()


def MakeGoalPmf(suite):
    metapmf = thinkbayes.Pmf()
    for lam, prob in suite.Items():
        pmf = MakePoissonPmf(lam)                                 # MakePoissonPmf
        metapmf.Set(pmf, prob)
    mix = MakeMixture(metapmf)                                    # MakeMixture
    return mix

def MakePoissonPmf(lam, high=10, n=101):
    pmf = thinkbayes.Pmf()
    for x in xrange(0,1+high):
        p = EvalPoissonPmf(lam, x)                                #EvalPoissonPmf
        pmf.Set(x, p)
    return pmf

def MakeMixture(metapdf):
    mix = thinkbayes.Pmf()
    for pmf, p1 in metapdf.Items():
        for x, p2 in pmf.Items():
            mix.Incr(x, p1*p2)
    return mix


def MakeGaussianPmf(mu, sigma, nsigma, n=101):
    pmf = thinkbayes.Pmf()
    low = mu - nsigma*sigma
    high = mu + nsigma*sigma

    for x in numpy.linspace(low, high, n):
        p = scipy.stats.norm.pdf(x, mu, sigma)
        pmf.Set(x, p)
    pmf.Normalize()
    return pmf

def EvalPoissonPmf(lam, k):
    return (lam)**k * math.exp(-lam) / math.factorial(k)



def main():
    h1 = Hockey()
    h2 = Hockey()
    h1.UpdateSet([0,2,8,4])
    h2.UpdateSet([0,1,2,3])
    h1 = MakeGoalPmf(h1)
    h2 = MakeGoalPmf(h2)

    thinkplot.Clf()
    thinkplot.preplot(num=2)
    thinkplot.Pmf(h1)
    thinkplot.Pmf(h2)
    thinkplot.Save(root='hockey_self5_MakeGoalPmf',xlabel='',ylabel='Probability',formats=['pdf'])

if __name__=="__main__":
    main()




