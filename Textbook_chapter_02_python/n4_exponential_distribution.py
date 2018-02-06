import numpy as np
from scipy.stats import expon
from matplotlib import pyplot as plt

# Define the distribution parameters to be plotted
theta_values = [1,5,10]
linestyles = ['-','--',':']
Color = ['black','blue','red']
#------------------------------------------------------------
# plot the distributions
#   we generate it using scipy.stats.poisson().  Once the distribution
#   object is created, we have many options: for example
#   - dist.pmf(x) evaluates the probability mass function in the case of
#     discrete distributions.
#   - dist.pdf(x) evaluates the probability density function for
#   evaluates
#fig, ax = plt.subplots(figsize=(5, 3.75))

for THETA, ls, COLOR in zip(theta_values, linestyles, Color):
    # create a poisson distribution
    # we could generate a random sample from this distribution using, e.g.
    #   rand = dist.rvs(1000)
    dist = expon(0,THETA)
    x = np.arange(-1, 200)

    plt.plot(x, dist.pdf(x), ls=ls, color=COLOR,
             label=r'$\theta=%i$' % THETA, linestyle='steps-mid')

plt.xlim(-0.5, 30)
plt.ylim(0, 0.4)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu)$')
plt.title('Poisson Distribution')

plt.legend()
plt.show()
