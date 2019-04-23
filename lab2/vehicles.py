import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed()  # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    df["Index"]=np.arange(df.shape[0])
    print(df.size)
    print((df.columns))
    sns_plot = sns.lmplot(df.columns[2], df.columns[1], data=df, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("./vehicles result/scaterplot2.png", bbox_inches='tight')


    CurntFlet = df.values.T[0]
    NewFlet = df.values.T[1][:79]

    print((("Mean Current Fleet : %f") % (np.mean(CurntFlet))))
    print((("Median Current Fleet: %f") % (np.median(CurntFlet))))
    print((("Var Current Fleet: %f") % (np.var(CurntFlet))))
    print((("std Current Fleet: %f") % (np.std(CurntFlet))))
    print((("MAD Current Fleet: %f") % (mad(CurntFlet))))

    print((("Mean New Fleet : %f") % (np.mean(NewFlet))))
    print((("Median New Fleet: %f") % (np.median(NewFlet))))
    print((("Var New Fleet: %f") % (np.var(NewFlet))))
    print((("std New Fleet: %f") % (np.std(NewFlet))))
    print((("MAD New Fleet: %f") % (mad(NewFlet))))



    plt.clf()
    sns_plot2 = sns.distplot(CurntFlet, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('Current Fleet')
    axes.set_ylabel('count')
    sns_plot2.savefig("./vehicles result/histogram Current Fleet .png", bbox_inches='tight')


    plt.clf()
    sns_plot3 = sns.distplot(NewFlet, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('New Fleet')
    axes.set_ylabel('count')
    sns_plot3.savefig("./vehicles result/histogram New Fleet .png", bbox_inches='tight')
