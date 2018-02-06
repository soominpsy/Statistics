"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf


class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    def __init__(self, hypos):
        """Initialize self.

        hypos: sequence of string bowl IDs
        """
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()
#        print "1",self.Items()
#        print "2", self.Values()        

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
#        print "3", self.Items()

    mixes = {
        'Bowl 1':dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2':dict(vanilla=0.5, chocolate=0.5),
        }

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
#        print "5", mix
        like = mix[data]
#        print "4", like
        return like

def main():
    hypos = ['Bowl 1', 'Bowl 2']

    pmf = Cookie(hypos)

#    pmf.Update('vanilla')

#    for hypo, prob in pmf.Items():
#        print hypo, prob
	
    datasets = ['vanilla','vanilla','vanilla']
    for data in datasets:
        pmf.Update(data)
        for hypo, prob in pmf.Items():
            print hypo, prob

if __name__ == '__main__':
    main()
