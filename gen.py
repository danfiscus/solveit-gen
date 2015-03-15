# -*- coding: utf-8 -*-
from random import uniform
from math import sin, pi
alpha = uniform(0,pi)
beta  = uniform(0,pi-alpha)
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
gamma≈%sradians≈%sdegress
""" % (a, b, c, alpha, alpha/pi*180, beta, beta/pi*180, gamma, gamma/pi*180)
