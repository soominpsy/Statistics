
import random

import thinkbayes
import thinkplot

FORMATS = ['pdf', 'eps', 'png']


class Die(thinkbayes.Pmf):
    """Represents the PMF of outcomes for a die."""

    def __init__(self, sides, name=''):
        """Initializes the die.

        sides: int number of sides
        name: string
        """
        thinkbayes.Pmf.__init__(self, name=name)
        for x in xrange(1, sides+1):
            self.Set(x, 1)
        self.Normalize()


def PmfMax(pmf1, pmf2):
    """Computes the distribution of the max of values drawn from two Pmfs.

    pmf1, pmf2: Pmf objects

    returns: new Pmf
    """
    res = thinkbayes.Pmf()
    i = 0
    j = 0 
    for v1, p1 in pmf1.Items():
        i = i + 1
        print(v1, p1)
        for v2, p2 in pmf2.Items():
            j = j + 1
            res.Incr(max(v1, v2), p1*p2)
#            print res.Items()
    print res.Items()
    print i
    print j
    return res



def main():
    d6 = Die(6, 'd6')
#    dice = [d6] * 3
    three_exact = d6 + d6 + d6
    best_attr2 = PmfMax(three_exact, three_exact) 



if __name__=="__main__":
    main()



