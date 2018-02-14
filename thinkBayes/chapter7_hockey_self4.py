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

def MakeGoalPmf(suite):
    metapmf = thinkbayes.Pmf()
    for lam, prob in suite.Items():
        pmf = MakePoissonPmf(lam, 10)              # MakePoissonPmf
        metapmf.Set(pmf, prob)
    mix = MakeMixture(metapmf)                     #MakeMixture
    return mix

def MakePoissonPmf(lam, high):
    pmf = thinkbayes.Pmf()
    for k in xrange(0,high+1):
        p = EvalPoissonPmf(lam, k)
        pmf.Set(k,p)
    pmf.Normalize()
    return pmf

def MakeMixture(metapmf):
    mix = thinkbayes.Pmf()
    for pmf, p1 in metapmf.Items():
        for x,p2 in pmf.Items():
            mix.Incr(x, p1*p2)
    return mix


def main():
    p1 = Hockey()
    p2 = Hockey()

    thinkplot.Clf()
    thinkplot.Pmf(p1)
    thinkplot.Pmf(p2)
    thinkplot.Save(root='hockey_self4_prior',xlabel='',ylabel='Probability',formats=['pdf'])

    p1.UpdateSet([0,2,8,4])
    p2.UpdateSet([1,3,1,0])
#    p2.UpdateSet([1,3,1,0,1,2,3,4,1,2,2,3,1,2,4,1,3,2,1,1,2,2,1,3,3,1,1,2,4,1,2,1,2,1,4,2,3,1,1])
    thinkplot.Clf()
    thinkplot.preplot(num=2)
    thinkplot.Pmf(p1)
    thinkplot.Pmf(p2)
    thinkplot.Save(root='hockey_self4_posterior',xlabel='',ylabel='Probability',formats=['pdf'])

    p1 = MakeGoalPmf(p1)
    p2 = MakeGoalPmf(p2)
    thinkplot.Clf()
    thinkplot.preplot(num=2)
    thinkplot.Pmf(p1)
    thinkplot.Pmf(p2)
    thinkplot.Save(root='hockey_self4_MakeGoalPmf',xlabel='',ylabel='Probability',formats=['pdf'])

if __name__=="__main__":
    main()




