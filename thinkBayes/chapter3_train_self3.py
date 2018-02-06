
from thinkbayes import Suite,Pmf

class Train(Suite):
    def __init__(self, hypos, alpha=1):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, hypo**(-1))
        self.Normalize()


    def Likelihood(self,data,hypo):
        if(hypo<data):
            return 0
        else:
            return 1.0/hypo


    
def main():
    suite = Train(range(1,501))
    for data in [30,60,90]:
        suite.Update(data)
    print suite.Mean()

    suite1= Train(range(1,1001))
    for data in [30,60,90]:
        suite1.Update(data)
    print suite1.Mean()

    suite2= Train(range(1,1001))
    for data in [30,60,90]:
        suite2.Update(data)
    print suite2.Mean()

    suite3= Train(range(1,100001))
    for data in [30,60,90]:
        suite3.Update(data)
    print suite3.Mean()
 
    cdf = suite3.MakeCdf()
    interval = cdf.Percentile(5), cdf.Percentile(95)
    print type(interval)
    print interval


if __name__=='__main__':
    main()






