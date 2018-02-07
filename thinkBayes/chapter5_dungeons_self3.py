from thinkbayes import Pmf
import thinkbayes
import thinkplot

class Die(Pmf):
    def __init__(self, sides):
        Pmf.__init__(self)
        for side in xrange(1, sides+1):
            self.Set(side,1)
        self.Normalize()


def main():
    d6 = Die(6)
    three_d6 = d6 + d6 + d6

    thinkplot.PrePlot(1)
    thinkplot.Pmf(three_d6)
    thinkplot.Save(root='dice_self3',xlabel='sum of dice',ylabel='Probability',formats=['pdf'])


if __name__=="__main__":
    main()







