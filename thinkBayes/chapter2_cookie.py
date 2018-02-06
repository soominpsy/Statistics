from thinkbayes import Pmf

pmf = Pmf()
pmf.Set('b1', 0.5)
pmf.Set('b2', 0.5)
print pmf.Items()

pmf.Mult('b1', 0.75)
pmf.Mult('b2', 0.5)
print pmf.Items()

pmf.Normalize()
print pmf.Items()
print pmf.Prob('b1')


