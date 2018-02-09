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



def main():
    data = ReadData()
    cols = zip(*data)
    price1, price2, bid1, bid2, diff1, diff2 = cols

    pdf = thinkbayes.EstimatedPdf(price1)
#    print(type(pdf))
    low, high = 0, 75000
    n = 101
    xs = numpy.linspace(low,high,n)
#    print(pdf.Density(25000))
    pmf = pdf.MakePmf(xs)


    thinkplot.PrePlot(1)
    thinkplot.Pmf(pmf)
    thinkplot.Save(root='price_self2',xlabel='',ylabel='Probability_density',formats=['pdf'])



if __name__=="__main__":
    main()









