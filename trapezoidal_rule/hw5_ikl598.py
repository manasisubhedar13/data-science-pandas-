#To run:  mpiexec -n 4 python Assignment_5_Trap_Rule.py 1.0 5.0 10000

import numpy
import sys
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

m = float(sys.argv[1])
n = float(sys.argv[2])
num = int(sys.argv[3])
dest = 0

def f(x):
        return 3*x*x

def integral(m, n, num):
    integral_value = -(f(m) + f(n))/2.0
    for x in numpy.linspace(m,n,num+1):
        integral_value += f(x)
    integral_value = integral_value * (n-m)/num
    return integral_value

my_int = numpy.zeros(1)
int_sum = numpy.zeros(1)


ht = (n - m) / num 
n_i =  num/size
a_i = m + rank * ht * n_i
b_i = a_i + n_i*ht
my_int[0] = integral(a_i,b_i,n_i)

print("The Process for trapezoidal rule ", rank, " has the partial integral collective communication ", my_int[0])
comm.Reduce(my_int, int_sum, MPI.SUM, dest)


if comm.rank == 0:
    print('The Integral Sum - Trapezoidal Area =', int_sum[0])

