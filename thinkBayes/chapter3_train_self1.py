from thinkbayes import Suite
import thinkplot 

class Train(Suite):
    def Likelihood(self, data, hypo):
        if(hypo<data):
            return 0
        else:
            return 1.0/hypo


def main():
    suite=Train(range(0,101))
    trainNum = [6,10,20,12,15,19,4,10]
#	suite.Update(60)
    for TN in trainNum:
        suite.Update(TN)
    suite.Print()    

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Save(root='train_self1', xlabel='Number of trains', ylabel='Probability',formats=['pdf'])


if __name__== '__main__':
    main()



