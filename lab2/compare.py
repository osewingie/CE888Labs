import numpy as np
import pandas as pd

def abTest(sample1,sample2,iterations,Tobs):
    if (Tobs == None):
        Tobs = np.mean(sample2)-np.mean(sample1)
    s1 = sample1.shape[0]
    s2 = sample2.shape[0]

    concat = np.concatenate((sample1, sample2), axis=0)

    passedIterations = 0

    for i in range(iterations):
        np.random.shuffle(concat)
        sample1_new = concat[0:s1]
        sample2_new = concat[s1:]


        Tprem = np.mean(sample2_new) - np.mean(sample1_new)

        if(Tprem >= Tobs):
            passedIterations = passedIterations+1

    pValue = passedIterations/iterations
    return pValue





df = pd.read_csv('./vehicles.csv')
sample1 = df.values.T[0]
sample2 = df.values.T[1][0:79]
abTestVal = abTest(sample1,sample2,10000,None)
print(abTestVal)
