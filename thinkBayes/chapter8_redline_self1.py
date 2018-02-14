import thinkbayes
import thinkplot
import numpy
import math
import random
import sys
import scipy

OBSERVED_GAP_TIMES = [
    428.0, 705.0, 407.0, 465.0, 433.0, 425.0, 204.0, 506.0, 143.0, 351.0,
    450.0, 598.0, 464.0, 749.0, 341.0, 586.0, 754.0, 256.0, 378.0, 435.0,
    176.0, 405.0, 360.0, 519.0, 648.0, 374.0, 483.0, 537.0, 578.0, 534.0,
    577.0, 619.0, 538.0, 331.0, 186.0, 629.0, 193.0, 360.0, 660.0, 484.0,
    512.0, 315.0, 457.0, 404.0, 740.0, 388.0, 357.0, 485.0, 567.0, 160.0,
    428.0, 387.0, 901.0, 187.0, 622.0, 616.0, 585.0, 474.0, 442.0, 499.0,
    437.0, 620.0, 351.0, 286.0, 373.0, 232.0, 393.0, 745.0, 636.0, 758.0,
]
#print(OBSERVED_GAP_TIMES)
print "cumulated data number :", len(OBSERVED_GAP_TIMES)

#OBSERVED_GAP_TIMES = OBSERVED_GAP_TIMES/60        # this is not working...
for i in xrange(0,len(OBSERVED_GAP_TIMES)):
    OBSERVED_GAP_TIMES[i] = OBSERVED_GAP_TIMES[i]/60
#print(OBSERVED_GAP_TIMES)

cdf_z = thinkbayes.MakeCdfFromList(OBSERVED_GAP_TIMES)
sample_z = cdf_z.Sample(220)
pmf_z = thinkbayes.MakePmfFromList(sample_z)
#pmf_z = scipy.stats.gaussian_kde(sample_z)


thinkplot.Clf()
thinkplot.preplot(2)
thinkplot.Clf()
thinkplot.Pmf(pmf_z)
thinkplot.Save(root='chapter8_self1',xlabel='',ylabel='Probability',formats=['pdf'])




