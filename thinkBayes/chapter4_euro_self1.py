import thinkplot
from thinkbayes import Suite, Pmf

class Euro(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Likelihood(self, data, hypo):
        x = hypo
        if ( data == 'H'):
            return x / 100.0
        else:
            return (100.0-x)/100.0

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()


def main():
    pmf = Euro(xrange(0,101))
    dataset = 'H'*140 + "T"*110 
#    dataset = 'H' + 'T'
#    dataset = 'T'
    for data in dataset:
#        print(data)
        pmf.Update(data)
#	print pmf.Items()
#	print pmf.Mean()
    print pmf.Prob(80)


    thinkplot.PrePlot(1)
    thinkplot.Pmf(pmf)
    thinkplot.Save(root='coin_self1',xlabel='',ylabel='Probability',formats=['pdf'])



if __name__=="__main__":
    main()



