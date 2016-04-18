import glob
from pylab import *
import brewer2mpl

import sys

 # brewer2mpl.get_map args: set name  set type  number of colors
bmap = brewer2mpl.get_map('Set1', 'qualitative', 5)
colors = bmap.mpl_colors
 
params = {
    'axes.labelsize': 8,
    'font.size': 8,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'figure.figsize': [4.5, 4.5]
}
rcParams.update(params)


def load(dir):
    f_list = glob.glob(dir + '/*/fitness.csv')
    num_lines = sum(1 for line in open(f_list[0]))
    i = 0;
    data = np.zeros((len(f_list), num_lines)) 
    for f in f_list:
        data[i, :] = np.loadtxt(f)[:,1]
        i += 1
    return data


data_hs = load('data/hs_cont/fitness')
data_ghs = load('data/ghs_cont/fitness')
data_ghs_1 = load('data/ghs_cont_1/fitness')
data_ghs_2 = load('data/ghs_cont_2/fitness')
data_ghs_3 = load('data/ghs_cont_3/fitness')
data_ghs_4 = load('data/ghs_cont_4/fitness')
data_ghs_5 = load('data/ghs_cont_5/fitness')
data_ghs_6 = load('data/ghs_cont_6/fitness')

n_generations = data_ghs.shape[1]
x = np.arange(0, n_generations)

# compute the median of each column
def med(data):
    median = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
    return median

med_hs = med(data_hs)
med_ghs = med(data_ghs)
med_ghs1 = med(data_ghs_1)
med_ghs2 = med(data_ghs_2)
med_ghs3 = med(data_ghs_3)
med_ghs4 = med(data_ghs_4)
med_ghs5 = med(data_ghs_5)
med_ghs6 = med(data_ghs_6)

fig = figure()

axes(frameon=0)
grid()

plot(x, med_hs, linewidth=2, color='#B22400')
plot(x, med_ghs, linewidth=2, linestyle='--', color='#006BB2')
plot(x, med_ghs1, linewidth=2, linestyle='-', color='b')
plot(x, med_ghs2, linewidth=2, linestyle='-.', color='g')
plot(x, med_ghs3, linewidth=2, linestyle='-', color='r')
plot(x, med_ghs4, linewidth=2, linestyle='-.', color='c')
plot(x, med_ghs5, linewidth=2, linestyle='--', color='m')
plot(x, med_ghs6, linewidth=2, linestyle='-.', color='y')


# xlim(70, n_generations)
# ylim(0.01, 0.1)

xlabel('Iterations')
ylabel('Objective Function')
title("Median plot",
         fontsize=10, weight='semibold')
legend = legend(["hs_cont", "ghs_cont", "ghs_cont_1", "ghs_cont_2", "ghs_cont_3", "ghs_cont_4", "ghs_cont_5", "ghs_cont_6"], loc=1);
# legend = legend(["ghs_cont", "ghs_cont_1", "ghs_cont_2", "ghs_cont_3", "ghs_cont_4", "ghs_cont_5", "ghs_cont_6"], loc=3);
# legend = legend(["hs_cont", "ghs_cont", "ghs_cont_m"], loc=2);
# legend = legend(["ghs_cont", "ghs_cont_m"], loc=2);
frame = legend.get_frame()
frame.set_facecolor('0.9')
frame.set_edgecolor('0.9')
# xticks(np.arange(0, 50, 5))
fig.tight_layout()
savefig('plots/median_sphere-1.png')
show()