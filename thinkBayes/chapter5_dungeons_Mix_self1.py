from thinkbayes import Pmf
import thinkbayes
import thinkplot

class Die(Pmf):
    def __init__(self, sides):
        Pmf.__init__(self)
        for side in xrange(1,sides+1):
            self.Set(side,1)
        self.Normalize()


def main():
    d6 = Die(6)
    d8 = Die(8)
    d12= Die(12) 
    d16= Die(16)
    d20= Die(20)

    mix = Pmf()
    for die in [d6,d8,d12,d16,d20]:
        for outcome, prob in die.Items():
            mix.Incr(outcome,prob)
    mix.Normalize()

    thinkplot.PrePlot(1)
    thinkplot.Pmf(mix)
    thinkplot.Save(root='dice_Mix_self1',xlabel='sum of dice',ylabel='Probability',formats=['pdf'])



if __name__=="__main__":
    main()
