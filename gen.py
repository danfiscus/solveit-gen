from random import uniform
from math import sin, pi
alpha = uniform(0,2*pi)
beta  = uniform(0,2*pi-alpha)
gamma = 2*pi-alpha-beta
c=uniform(0,2048)
a=c*sin(alpha)/sin(gamma)
b=c*sin(beta)/sin(gamma)
print """
a=%s
b=%s
c=%s
alpha=%sradians
beta=%sradians
gamma=%sradians
""" % (a, b, c, alpha, beta, gamma)
