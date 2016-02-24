import prettyplotlib as ppl
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)

data = np.random.randn(8, 4)
labels = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
ppl.boxplot(ax, data, xticklabels=labels)
fig.savefig('boxplot_prettyplotlib_default.png')