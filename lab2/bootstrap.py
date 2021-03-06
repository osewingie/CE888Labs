import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations,CI):
	diff = (100 - CI) / 2;
	samples = np.ndarray(shape=(iterations,sample_size))
	for i in range(iterations):
		samples[i]=np.random.choice(sample, sample_size)
	data_mean=np.mean(samples)
	means = np.mean(samples,axis=1)
	upper= np.percentile(means,100-diff)
	lower = np.percentile(means,diff)
	return data_mean, lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')

	data = df.values.T[0]
	boots = []

	testarry = np.array(range(1,100,1))
	x = np.percentile(testarry, 95)

	for i in range(100, 100000, 1000):
		boot = boostrap(data, data.shape[0], i,95)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])
		print(i)

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("./Bootstrap result/vehicle old fleet.png", bbox_inches='tight')


	print("Mean : %0.3f " % np.mean(data))
	print("Var  : %0.3f " % np.var(data))
