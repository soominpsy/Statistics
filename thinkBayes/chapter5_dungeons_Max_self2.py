from thinkbayes import Pmf
import thinkbayes
import thinkplot

'''
class MaxDie(Pmf):
    def __init__(self, sides):
        Pmf.__init__(self)
        for side in xrange(1+sides):
            self.Set(side,1)
        self.Normalize()
'''
class Cdf(Pmf):
    def Max(self,k):
        cdf = self.Copy()
        cdf.ps = [p**k for p in cdf.ps]
        return cdf






