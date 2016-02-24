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


data_hs = load('data/hs_2D_wp/fitness')
data_ghs = load('data/ghs_2D_wp/fitness')
data_ghs_m = load('data/ghs_m_2D_wp/fitness')

n_generations = data_hs.shape[1]
x = np.arange(0, n_generations)

# compute the median of each column
def med(data):
    median = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
    return median

med_hs = med(data_hs)
med_ghs = med(data_ghs)
med_ghs_m = med(data_ghs_m)

fig = figure()
xlim(-1, n_generations)
ylim(16000, 31000)

axes(frameon=0)
grid()

plot(x, med_hs, linewidth=2, color='#B22400')
plot(x, med_ghs, linewidth=2, linestyle='--', color='#006BB2')
plot(x, med_ghs_m, linewidth=2, linestyle='-.', color='#FF6BB2')

xlabel('Iterations')
ylabel('Objective Function')
title("Median plot",
         fontsize=10, weight='semibold')
# legend = legend(["Harmony Search", "Global Best HS"], loc=4);
legend = legend(["Harmony Search", "Global Best HS", "Modified GHS"], loc=4);
frame = legend.get_frame()
frame.set_facecolor('0.9')
frame.set_edgecolor('0.9')
# xticks(np.arange(0, 50, 5))
fig.tight_layout()
# savefig('plots/HS_GHS_median.png')
savefig('plots/HS_GHS_mGHS_median.png')
show()