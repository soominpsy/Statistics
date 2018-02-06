from chapter3_dice import Dice
import thinkplot

class Train(Dice):
    """
    """

def main():
    hypos = range(1,1001)
    suite = Train(hypos)
    
    suite.Update(60)
    print suite.Mean()

    thinkplot.PrePlot(1)
    thinkplot.Pmf(suite)
    thinkplot.Save(root='train_self2',xlabel='Number of trains',ylabel='Probability',formats=['pdf'])


if __name__=="__main__":
    main()




