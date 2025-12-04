from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def mc_pi(nsamp) :
    total = 0
    delta = 1000000
    count = 0
    nloops = nsamp/delta
    rng = np.random.default_rng(rank)
    for i in range(int(nloops)) :
        nextsamp = delta
        sampx = rng.random(nextsamp)
        sampy = rng.random(nextsamp)
        accept = (sampx**2 + sampy**2) < 1.0
        count += np.count_nonzero(accept)
        total += delta
    return 4*count/total

if rank == 0:
    print("Size: ", comm.Get_size())
nsamp = 1000000000
my_samps=nsamp/comm.Get_size()

my_pi = mc_pi(my_samps)
# Create some np arrays on each process:
# For this demo, the arrays have only one
# entry that is assigned to be the rank of the processor
value = np.array(my_pi)

print(' Rank: ',rank, ' value = ', value)

# initialize the np arrays that will store the results:
value_sum      = np.array(0.0,'d')

# perform the reductions:
comm.Reduce(value, value_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(value_sum/comm.Get_size())

