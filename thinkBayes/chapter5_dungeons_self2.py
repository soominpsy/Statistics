import thinkbayes
from thinkbayes import Pmf 
import thinkplot

class Die(Pmf):
    def __init__(self, sides):
        Pmf.__init__(self)
        for x in xrange(1,sides+1):
            self.Set(x,1)
        self.Normalize()

def SampleSum(dists, n):
    pmf = thinkbayes.MakePmfFromList(RandomSum(dists) for i in xrange(n))
    return pmf

def RandomSum(dists):
    total = sum(dist.Random() for dist in dists)
    print(total)
    return total



def main():
    d6 = Die(6)
    dice = [d6] * 3
    dice1 = [d6] * 1
    print type(d6)
    print d6.Items()
    print type(dice)
    print dice[0].Items()
    print dice[1].Items()
    print dice[2].Items()

#    t1 = RandomSum(dice)
    test = SampleSum(dice,50)

    thinkplot.PrePlot(1)
    thinkplot.Pmf(test)
    thinkplot.Save(root='dice_self2',xlabel='sum of dice',ylabel='Probability',formats=['pdf'])

if __name__=="__main__":
    main()


