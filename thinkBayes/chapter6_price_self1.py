import thinkbayes
import thinkplot
import numpy
import csv
import matplotlib.pyplot as pyplot
import scipy

def ReadData(filename='showcases.2011.csv'):
    fp = open(filename)
    reader = csv.reader(fp)
#    print(type(reader))
    res = []
    res_self = []
    for t in reader:
        _heading = t[0]
        data = t[1:]
        data2= t[2:]
        try:
            data = [int(x) for x in data]
            res.append(data)
            res_self.append(data)
            data2 = [int(y) for y in data2]
            res_self.append(data2)
        except ValueError:
            pass

    print(type(res))
    print(len(res))
    print(type(res_self))
    print(len(res_self))
    fp.close()
    return zip(*res)


class EstimatedPDF(thinkbayes.Pdf):
    def __init__(self, sample):
        self.kde = scipy.stats.gaussian_kde(sample)
    def Density(self,x):
        return self.kde.evaluate(x)





def main():
    prices = ReadData()


if __name__=="__main__":
    main()









