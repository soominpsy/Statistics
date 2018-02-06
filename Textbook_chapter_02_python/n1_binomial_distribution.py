# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general
import numpy as np
from scipy.stats import binom
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.
#from astroML.plotting import setup_text_plots
#setup_text_plots(fontsize=8, usetex=True)

#------------------------------------------------------------
# Define the distribution parameters to be plotted
n_values = [20, 20, 40]
p_values = [0.2, 0.6, 0.6]
linestyles = ['-', '--', ':']
color = ['black','blue','red']
x = np.arange(-1, 200)

#------------------------------------------------------------
# plot the distributions
#fig, ax = plt.subplots(figsize=(5, 3.75))

for (n, p, LS, COLOR) in zip(n_values, p_values, linestyles, color):
    # create a binomial distribution
    dist = binom(n, p)
#    plt.plot(x, dist.pmf(x))
    plt.plot(x, dist.pmf(x), ls=LS, c=COLOR,
             label=r'$p=%.1f,\ n=%i$' % (p, n), drawstyle='steps-mid') #linestyle='steps-mid')

plt.xlim(-0.5, 35)
plt.ylim(0, 0.25)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|b, n)$')
plt.title('Binomial Distribution')

plt.legend()
plt.show()
