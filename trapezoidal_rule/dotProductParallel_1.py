#dotProductParallel_1.py
#"to run" syntax example: mpiexec -n 4 python26 dotProductParallel_1.py 40000
from mpi4py import MPI
import numpy as np
import math
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#read from command line
n = int(sys.argv[1])    #length of vectors

#arbitrary example vectors, generated to be evenly divided by the #number of processes for convenience

x = np.linspace(0,100,n) if comm.rank == 0 else None
y = np.linspace(20,300,n) if comm.rank == 0 else None

#initialize as numpy arrays
dot = np.array([0.])
local_n = np.array([0])

#test for conformability
if rank == 0:
         '''if (n != y.size):
                  print("vector length mismatch")
                  comm.Abort()

         #currently, our program cannot handle sizes that are not evenly divided by the number of processors
         if(n % size != 0):
                   print("the number of processors must evenly divide n.")
                   comm.Abort()'''

         #length of each process's portion of the original vector
         print("n = %s, size = %s" % (n, size))
         local_n = np.array([math.floor(n/size)])



#communicate local array size to all processes
comm.Bcast(local_n, root=0)



#initialize as numpy arrays
local_x = np.zeros(local_n)
local_y = np.zeros(local_n)

#divide up vectors
#comm.Scatter(x, local_x, root=0)
#comm.Scatter(y, local_y, root=0)

#send data using scatterv()
comm.Scatterv([x,(40000),(0),MPI.DOUBLE],local_x,root=0)
comm.Scatterv([y,(40000),(0),MPI.DOUBLE],local_y,root=0)

#local computation of dot product
local_dot = np.array([np.dot(local_x, local_y)])

#sum the results of each
comm.Reduce(local_dot, dot, op = MPI.SUM)

if (rank == 0):
                print("The dot product is", dot[0], "computed in parallel")
                print("and", np.dot(x,y), "computed serially")
