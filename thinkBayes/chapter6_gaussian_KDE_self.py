import scipy
import thinkbayes
from thinkbayes import Pdf

class EstimatedPdf(Pdf):
    def __init__(self, sample):
        self.kde = scipy.stats.gaussian_kde(sample)
    def Density(self, x):
        return self.kde.evaluate(x)




