# -*- coding: utf-8 -*-
from random import uniform
from math import sin, pi
bounds = 0.1
alpha = uniform(bounds,pi-2*bounds)
beta  = uniform(bounds,pi-alpha-2*bounds)
gamma = pi-alpha-beta
c=uniform(0,2048)
a=c*sin(alpha)/sin(gamma)
b=c*sin(beta)/sin(gamma)
print """
a≈%s
b≈%s
c≈%s
alpha≈%sradians≈%sdegrees
beta≈%sradians≈%sdegrees
gamma≈%sradians≈%sdegrees
""" % (a, b, c, alpha, alpha/pi*180, beta, beta/pi*180, gamma, gamma/pi*180)
