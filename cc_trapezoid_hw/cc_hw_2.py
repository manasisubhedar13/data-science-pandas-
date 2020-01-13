from math import *
# define a function to be integrated
def f(x):
	return 3*(x**2)

#this is the serial version of the trapezoidal rule.
#parallelization occurs by dividing the range among processes.
def trap(f, upper_bound, lower_bound, number_of_polygons):

	a = (upper_bound-lower_bound)/float(number_of_polygons)
	b = 0.5*(f(lower_bound) + f(upper_bound))
	for i in range(1,number_of_polygons,1):
		b += f(lower_bound + i*a)

	return a*b

def error(approx):
	err = approx - 124 
	return err

lower_bound = int(raw_input("please enter Lower bound:"))

upper_bound = int(raw_input("please enter the Upper bound:"))

number_of_polygons = int(raw_input("please enter the number of polygons:"))

number = trap(f,upper_bound,lower_bound,number_of_polygons)
err = error(number)
print "Area of the trapezoid : " + str(number)
print "Error : " + str(err)
