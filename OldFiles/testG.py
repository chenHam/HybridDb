import matplotlib.pyplot as plt
import pandas as pd

def main():
    # dfA = pd.read_csv('testA.csv')
    # dfB = pd.read_csv('testB.csv')
    # dfC = pd.read_csv('testC.csv')
    #
    # data = dfA[['time','A']].plot()
    # data = dfB[['time','A']].plot()
    # data = dfC[['time','A']].plot()

    # dfB[['time','A']].plot('time','A',label="Thin",marker='',color='green')
    # dfC[['time','A']].plot('time','A',label="test",marker='',color='pink')
    dfABC = pd.read_csv('testABC.csv')
    dfABC[['A','B','C']].plot()

    plt.xlabel("Time from beginning")
    plt.ylabel("Total time completed")
    plt.show()


main()