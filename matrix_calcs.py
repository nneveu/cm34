import numpy as np

# Constants
l1 = 2.4 # m
l2 = 1.5 # m 
# Converting Gauss-m to T-m
kx = 0.0019  # T-m = 19  G-m
ky = -0.0025 # T-m = -25 G-m 
cl = 0.1 # corrector length in meters

# Multiply field strength by length to get T units
# Assuming momentum and kinetic energy differences are neglible (electrons)
def calc_rho_theta(energy, k, l):
    rho   = energy / (0.3*k*l)
    theta = l/rho
    print('rho', rho, 'theta', theta)
    return rho, theta

energy = 0.60 # GeV (60 MeV)
rhox, thetax = calc_rho_theta(energy, kx, cl) 
rhoy, thetay = calc_rho_theta(energy, ky, cl)

# Initial conditions
xinit_offset = 0.001 #m - Say we start w/ 1 mm offset
xinit_angle  = 0.01  #Say we start with a very small angle (best case)

yinit_offset = 0.001 #m - Say we start w/ 1 mm offset
yinit_angle  = 0.0  #Say we start with no angle (best case)

x0 = np.array([[xinit_offset],
               [xinit_angle]])

y0 = np.array([[yinit_offset],
               [yinit_angle]])

m_d1 = np.array([[1, l1],
                 [0, 1]])

m_d2 = np.array([[1, l2],
                 [0, 1]])

#q_cmx = np.array([[1, 0],
#                 [klx, 1]])
#
#q_cmy = np.array([[1, 0],
#                 [kly, 1]])

c_cmx = np.array([[1, rhox*np.sin(thetax)],
                 [0, 1]])

c_cmy = np.array([[1, rhoy*np.sin(thetay)],
                 [0, 1]])

def calc_offsets(minitial, m_d1, m_d2, q_cm):
    xd2_q1    = np.matmul(m_d2, q_cm)
    xd2_q1_d1 = np.matmul(xd2_q1, m_d1)
    #note, this can return x or y depending on what you supply in initial and q_cm
    x2_xp2    = np.matmul(xd2_q1_d1, minitial)
    return x2_xp2

xoffsets = calc_offsets(x0, m_d1, m_d2, c_cmx)
yoffsets = calc_offsets(y0, m_d1, m_d2, c_cmy) 

print('Beam offset at CM34 in x: ', xoffsets[0][0]*1000, 'mm')
print('Beam offset at CM34 in y: ', yoffsets[0][0]*1000, 'mm')
