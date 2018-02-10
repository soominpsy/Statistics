import numpy
import scipy
import thinkbayes
import thinkplot

def MakeGaussianPmf(mu, sigma, num_sigmas, n=101):
    pmf = thinkbayes.Pmf()
    low = mu - num_sigmas*sigma
    high = mu + num_sigmas*sigma

    for x in numpy.linspace(low, high, n):
        p = scipy.stats.norm.pdf(mu, sigma, x)
        pmf.Set(x, p)
    pmf.Normalize()
    return pmf




def main():
    PMF = MakeGaussianPmf(20,5,2,n= 101)


if __name__=="__main__":
    main()

