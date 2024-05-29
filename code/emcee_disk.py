import numpy as np

obs = np.loadtxt('disk.csv', delimiter=",")
zObs = obs[:,0]
rhoObs = obs[:,1]

# Two component model of the vertical structure of a disk:
# returns rho(z) for model parameters midplane density and scale height
# of a thin plus thick disk
def rho_model(z, rho_thin, h_thin, rho_thick, h_thick) :
    thin = rho_thin/np.cosh(z/h_thin)**2
    thick = rho_thick/np.cosh(z/h_thick)**2
    return thin + thick

# Given model parameters theta, return least squares assuming equal errors
# on all points
def lsq_opt(theta) :
    rho_thin, h_thin, rho_thick, h_thick = theta
    # print(h_thin, h_thick)
    # WARNING: bad form!: using global variables rhoObs and zObs
    return np.sum((rhoObs - rho_model(zObs, rho_thin, h_thin, rho_thick,
                                      h_thick))**2)

from scipy.optimize import minimize

soln = minimize(lsq_opt, [1e-3, 1000.0, 1e-3, 1000.], method="Powell")

print(soln)

# return log(likelihood) given model parameters
def log_likehood(theta) :
    rho_thin, h_thin, rho_thick, h_thick = theta

# For EMCEE to work, priors need to be set to limit the search range
    if not (0.0 < rho_thin < 0.01 and 0.0 < h_thin < 2e3
            and 0.0 < rho_thick < 0.01 and 0.0 < h_thick < 2e3) :
        return -np.inf
# And a prior encoding the mean of thick and thin:
#    if h_thin > h_thick:
#        return -np.inf

    ll = -np.log(lsq_opt(theta))
        
    return ll

# 32 walkers in a small Gaussian ball around the Powell Minimum.
pos = soln.x + soln.x*1e-4 * np.random.randn(32, 4)
nwalkers, ndim = pos.shape

import emcee
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_likehood)
sampler.run_mcmc(pos, 100000, progress=True)

flat_samples = sampler.get_chain(discard=1, thin=15, flat=True)

labels = ["$\\rho_{thin}$", "$h_{thin}$", "$\\rho_{thick}$", "$h_{thick}$"]

# Produce a corner plot
import corner

corner.corner(flat_samples,labels=labels)
