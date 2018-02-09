import thinkbayes
import thinkplot
import numpy
import csv
import matplotlib.pyplot as pyplot
import scipy
from thinkbayes import Pmf

def ReadData(filename='showcases.2011.csv'):
    fp = open(filename)
    reader = csv.reader(fp)
    res = []
    res_self = []
    for t in reader:
        _heading = t[0]
        data = t[1:]
        try:
            data = [int(x) for x in data]
            res.append(data)
        except ValueError:
            pass

    fp.close()
    return zip(*res)


class Pdf(object):
    def Density(self, x):
        raise UnimplementedMethodException()
    def MakePmf(self,xs):
        pmf = Pmf()
        for x in xs:
            pmf.Set(x, self.Density(x))
        pmf.Normalize()
        return pmf


class EstimatedPdf(Pdf):
    def __init__(self, sample):
        self.kde = scipy.stats.gaussian_kde(sample)
    def Density(self,x):
        return self.kde.evaluate(x)

class GaussianPdf(Pdf):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
    def Density(self, x):
        return scipy.stats.norm.pdf(x, self.mu, self.sigma)


class Player(object):
    n = 101
    price_xs = numpy.linspace(0, 75000, n)

    def __init__(self, prices, bids, diffs):
        self.pdf_price = EstimatedPdf(prices)
        self.cdf_diff = thinkbayes.MakeCdfFromList(diffs)
        mu =0
        sigma = numpy.std(diffs)
        self.pdf_error = GaussianPdf(mu, sigma)

    def ErrorDensity(self, error):
        return self.pdf_error.Density(error)

    def PmfPrice(self):
        return self.pdf_price.MakePmf(self.price_xs)

    def MakeBeliefs(self, guess):
        pmf = self.PmfPrice()
        self.prior = Price(pmf, self)
        self.posterior = self.prior.Copy()
        self.posterior.Update(guess)
        print(self.posterior)

class Price(thinkbayes.Suite):
    def __init__(self,pmf, player):
        thinkbayes.Suite.__init__(self,pmf)
        self.player = player

    def Likelihood(self, data, hypo):
        price = hypo
        guess = data
        error = price - guess
        like = self.player.ErrorDensity(error)
        return like




def main():
    data = ReadData()
    cols = zip(*data)
    price1, price2, bid1, bid2, diff1, diff2 = cols
#    print(type(price1))
#    print(price1)

    pdf = EstimatedPdf(price1)
    low, high = 0, 75000
    n = 101
    xs = numpy.linspace(low,high,n)
    pmf = pdf.MakePmf(xs)

    player1 = Player(price1, bid1, diff1)
    player2 = Player(price2, bid2, diff2)
#    PmfPlayer1 = player1.PmfPrice()
#    PmfPlayer2 = player2.PmfPrice()
    p1 = player1.MakeBeliefs(20000)
    p2 = player2.MakeBeliefs(40000)
#    print(type(p1))
#    print(p1)

#    price1 = Price(PmfPlayer1, player1)
#    like_test1 = price1.Likelihood(25000, 22000)
#    print(like_test1)




#    thinkplot.PrePlot(1)
#    thinkplot.Pmf(PmfPlayer1)
#    thinkplot.Save(root='price_self3',xlabel='',ylabel='Probability_density',formats=['pdf'])



if __name__=="__main__":
    main()









