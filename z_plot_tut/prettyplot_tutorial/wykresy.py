import prettyplotlib as ppl
import numpy as np

# prettyplotlib imports 
import matplotlib.pyplot as plt
import matplotlib as mpl
from prettyplotlib import brewer2mpl

# Set the random seed for consistency
np.random.seed(12)

fig, ax = plt.subplots(1)

# Show the whole color range
for i in range(8):
    y = np.random.normal(size=1000).cumsum()
    x = np.arange(1000)

    # For now, you need to specify both x and y :(
    # Still figuring out how to specify just one
    ppl.plot(ax, x, y, label=str(i), linewidth=0.75)

ppl.legend(ax)

fig.savefig('plot_prettyplotlib_default.png')

##########################################
import prettyplotlib as ppl
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)

data = np.random.randn(8, 4)
labels = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
ppl.boxplot(ax, data, xticklabels=labels)
fig.savefig('boxplot_prettyplotlib_default.png')

#########################################################
# Notice that this syntax is different from all others,
# because you must supply fig as well to plot the colormap,
# the scale which shows what color corresponds to what value.
import prettyplotlib as ppl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.random.randn(10,10))
fig.savefig('pcolormesh_prettyplotlib_default.png')

###
# It can be a pain in the neck to figure out how to put row and column labels
# directly onto a pcolormesh heatmap. Thankfully, prettyplotlib will
# accept xticklabels and yticklabels arguments, like this:
import prettyplotlib as ppl
import matplotlib.pyplot as plt
import numpy as np
import string

fig, ax = plt.subplots(1)

np.random.seed(10)

ppl.pcolormesh(fig, ax, np.random.randn(10,10), 
               xticklabels=string.uppercase[:10], 
               yticklabels=string.lowercase[-10:])
fig.savefig('pcolormesh_prettyplotlib_labels.png')