import numpy as np
import matplotlib.pyplot as plt

# hyperparams
N = 100                 # no. of iterations
resol = 200            # resolution of grid along one axis
seq = [1,0,1,1,0,1]     # variable sequence
x0 = 0.5                # initial value for recurrence relation

# recurrence relation for x_n
def f(x_n,r):
    return r*x_n*(1-x_n)

# derivative of recurrence relation wrt x_n
def f_prime(x_n,r):
    return r*(1-2*x_n)

# function for calculating the Lyapunov exponents
def lyapunov_exp(x_ns,rs):

    lyap_exp = 0

    for i in range(1,len(x_ns)):
        j = i%modulus_num         # taking into consideration for user specified sequence
        lyap_exp += np.log(abs(f_prime(x_ns[i], rs[j])))

    return lyap_exp/N

# function that generates the lyapunov diagram
def lyapunov_diagram(x_0 = 0):

    global modulus_num
    modulus_num = len(seq)

    r1 = np.linspace(0, 4, resol)
    r2 = np.linspace(0, 4, resol)
    rs_1,rs_2 = np.meshgrid(r1,r2)

    zs = np.zeros((resol,resol))
    lyap_exps = np.zeros((resol,resol))

    # looping over grid
    for i in range(0, resol):
        for j in range(0, resol):

            zs[i][j] = x_0
            rs = [(1-k)*r1[i] + k * r2[j] for k in seq]
            x_ns = []

            for iter in range(1,N):
                zs[i][j] = f(zs[i][j], rs[iter % modulus_num])          # calculating x_{n+1} given x_n
                x_ns.append(zs[i][j])                                   # appending to list

            lyap_exps[i][j] = lyapunov_exp(x_ns,rs)                     # using saved list of x_n's for given r_1 and r_2 to calculate lyapunov exp.

    # plotting the result
    plt.pcolormesh(r1,r2,lyap_exps, cmap = 'RdYlBu')
    plt.colorbar()
    plt.xlabel(r'$r_1$')
    plt.ylabel(r'$r_2$')
    plt.title('Lyapunov Diagram' + '\n' + r'$params: x_0 = {}, N = {}, resolution = {}$'.format(round(x_0,2), N,resol) + '\n' + r'$sequence = {}$'.format(seq))
    plt.show()

lyapunov_diagram(x_0 = x0)