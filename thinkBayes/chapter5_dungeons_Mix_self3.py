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
    pmf_dice = Pmf()
    pmf_dice.Set(Die(6),2)
    pmf_dice.Set(Die(8),3)
    pmf_dice.Set(Die(12),1)
    pmf_dice.Set(Die(20),1)
    
    mix = Pmf()
    for die, weight in pmf_dice.Items():
        for outcome, prob in die.Items():
            mix.Incr(outcome, weight*prob)
    mix.Normalize()

    thinkplot.PrePlot(1)
    thinkplot.Pmf(mix)
    thinkplot.Save(root='dice_Mix_self3',xlabel='',ylabel='Probability',formats=['pdf'])

if __name__=="__main__":
    main()
