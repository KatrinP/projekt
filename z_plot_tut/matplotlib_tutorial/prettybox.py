import glob

import prettyplotlib as ppl
import numpy as np
import matplotlib.pyplot as plt

from pylab import *

params = {
    'axes.labelsize': 8,
    'font.size': 8,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'figure.figsize': [2.5, 4.5]
}
rcParams.update(params)

def load(dir):
    f_list = glob.glob(dir + '/*/*/bestfit.dat')
    num_lines = sum(1 for line in open(f_list[0]))
    i = 0;
    data = np.zeros((len(f_list), num_lines)) 
    for f in f_list:
        data[i, :] = np.loadtxt(f)[:,1]
        i += 1
    return data

data_low_mut = load('data/low_mut')
data_high_mut = load('data/high_mut')
low_mut_100 = data_low_mut[:, 100]
high_mut_100 =  data_high_mut[:, 100]


fig, ax = plt.subplots()
ppl.boxplot(ax, [low_mut_100, high_mut_100])

fig.savefig('boxplot_prettyplotlib_default.png')