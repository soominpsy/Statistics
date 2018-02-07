from thinkbayes import Pmf
import thinkplot
import thinkbayes

class Die(Pmf):
    def __init__(self, sides):
        Pmf.__init__(self)
        for x in xrange(1,sides+1):
            self.Set(x,1)
        self.Normalize()

def main():
    d6 = Die(6)
    dice = [d6] * 3
    three = thinkbayes.SampleSum(dice, 1000)
    print(three.Items())

    thinkplot.PrePlot(1)
    thinkplot.Pmf(three)
    thinkplot.Save(root='dice_self1',xlabel='sum of dice',ylabel='Probability',formats=['pdf'])

if __name__=="__main__":
    main()



