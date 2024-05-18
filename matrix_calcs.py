import numpy as np

# Constants
l1 = 2.4 # m
l2 = 1.5 # m 
klx = 19  # G-m
kly = -25 # G-m

# Initial conditions
xinit_offset = 0.001 #m - Say we start w/ 1 mm offset
xinit_angle  = 0 # Say we start with no angle (best case)

yinit_offset = 0.001 #m - Say we start w/ 1 mm offset
yinit_angle  = 0 # Say we start with no angle (best case)

x0 = np.array([[xinit_offset],
               [0]])

y0 = np.array([[yinit_offset],
               [0]])

m_d1 = np.array([[1, l1],
                 [0, 1]])

m_d2 = np.array([[1, l1],
                 [0, 1]])

q_cmx = np.array([[1, 0],
                 [klx, 1]])

q_cmy = np.array([[1, 0],
                 [kly, 1]])

def calc_offsets(minitial, m_d1, m_d2, q_cm):
    xd2_q1    = np.matmul(m_d2, q_cm)
    xd2_q1_d1 = np.matmul(xd2_q1, m_d1)
    #note, this can return x or y depending on what you supply in initial and q_cm
    x2_xp2    = np.matmul(xd2_q1_d1, minitial)
    return x2_xp2

xoffsets = calc_offsets(x0, m_d1, m_d2, q_cmx)
yoffsets = calc_offsets(y0, m_d1, m_d2, q_cmy) 

print('Beam offset at CM34 in x: ', xoffsets[0][0]*1000, 'mm')
print('Beam offset at CM34 in y: ', yoffsets[0][0]*1000, 'mm')