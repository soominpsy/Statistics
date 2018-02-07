from thinkbayes import Pmf
import thinkbayes
import thinkplot

class Die(Pmf):
    def __init__(self,sides):
        Pmf.__init__(self)
        for side in xrange(1, sides+1):
            self.Set(side,1)
        self.Normalize()

def RandomMax(dists):
    total = max(dist.Random() for dist in dists)
#    print total
    return total

def sampleMax(dists, n):
    pmf = thinkbayes.MakePmfFromList(RandomMax(dists) for i in xrange(n))
    return pmf


def main():
    d6 = Die(6)
    dice1 = [d6] * 1
    dice3 = [d6] * 3
    RandomMax(dice3)
    test = sampleMax(dice3, 1000)

    thinkplot.PrePlot(1)
    thinkplot.Pmf(test)
    thinkplot.Save(root='diceMax_self1',xlabel='sum of dice',ylabel='Probability',formats=['pdf'])


if __name__=="__main__":
    main()





