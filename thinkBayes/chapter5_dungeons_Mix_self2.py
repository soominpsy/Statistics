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
#    d6 = Die(6)
#    d8 = Die(8)
    d6 = Pmf()
    print type(d6)
    d6.Set(Die(6),2)
    print type(d6)
    d8 = Pmf()
    d8.Set(Die(8),3)
    d12= Pmf()
    d12.Set(Die(12),1)
    d20=Pmf()
    d20.Set(Die(20),1)

    mix = Pmf()
    for dice in [d6, d8, d12, d20]:
#        print type(dice)
        for die, weight in dice.Items():
#            print type(die)
            for outcome, prob in die.Items():
                mix.Incr(outcome, weight*prob)
    mix.Normalize()    

    thinkplot.PrePlot(1)
    thinkplot.Pmf(mix)
    thinkplot.Save(root='dice_Mix_self2',xlabel='',ylabel='Probability',formats=['pdf'])

if __name__=="__main__":
    main()
