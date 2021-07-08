from sympy import *

# get contribution for degree 0 class
def phi_cpn(n):

    t = symbols('t0:%d'%(n+1))
    expr = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if i < j and j < (n - i - j):
                expr += t[i]*t[j]*t[n-i-j]
    
    for i in range(0, n): # todo: too long range
        if (2*i <= n) and (n != 3*i):
            expr += Pow(t[i],2)*t[n-2*i]/2
    
    if n % 3 == 0:
        expr += Pow(t[n/3], 3)

    return expr


print(phi_cpn(2))


def gw_potential(n):
    if n == 1:
        s, t0, t1 = symbols('s t0 t1')
        potential = Pow(t0, 2)*t1/2 + exp(t1)*s
        return potential
    elif n >= 2:
        expr = phi_cpn(n)
        

        return 0 
    else:
        return -1


# Gromov-Witten Invariant for CPn
# input1: k_ = [k_0, k_1, k_2,...,k_n] 
#          where k_2 is the number of degree 2 class,
#                k_3 is the number of degree 3 class,...etc
#          k_0 = k_1 = 0 are just dummy variable present so that
#          indexing the array is not so troublesome
# input2: d, the degree of rational curve
# input3: n, n for complex projective n space
def gw_cpn(k_, d, n):
    k = sun(k_)

    potential = gw_potential(n)

    


    return 0

    


def gw_cp1(k_, d):
    k = sum(k_)
    if k in [0, 1, 2]:
        return 1
    
    
    
        