import numpy as np
print("SCALAR")
s1 = np.array(3)
s2 = np.array(22)
s_sum = s1+s2
s_diff = s1-s2
s_prod = s1*s2
s_div = s1/s2
print("s1 = ", s1)
print("s2 = ", s2)
print("s1+s2 = ", s_sum)
print("s1-s2 = ", s_diff)
print("s1*s2 = ", s_prod)
print("s1/s2 = ", s_div)
print("")

print("VECTORS")
v1 = np.array([50, 60, 70, 80])
v2 = np.array([5, 6, 7, 8])
v_sum = v1+v2
v_diff = v1-v2
v_prod = v1*v2
v_div = v1/v2
dp = v1 @ v2.T
print("v1 = ", v1)
print("v2 = ", v2)
print("v1+v2 = ", v_sum)
print("v1-v2 = ", v_diff)
print("v1*v2 = ", v_prod)
print("v1/v2 = ", v_div)
print("v1.v2 = ", dp)
rd = np.random.default_rng()
r = rd.random(5)
print(r)
r = (r*1000)//10
print(r)
cryp = np.random.randint(0,2,256)
print(cryp)
print("")

print("MATRICES")
m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([1]) #for broadcasting
m_sum = m1+m2
m_diff = m1-m2
m_prod = m1*m2
m_div = m1/m2
print("m1 = ",m1)
print("m2 = ",m2)
print("m1+m2 = ",m_sum)
print("m1-m2 = ",m_diff)
print("m1*m2 = ",m_prod)
print("m1/m2 = ",m_div)
print("")

print("TENSOR")
t1 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
t2 = np.array([[[12,11,10],[9,8,7]],[[6,5,4],[3,2,1]]])
t_sum = t1+t2
t_diff = t1-t2
t_prod = t1*t2
t_div = t1/t2
print("t1 = ",t1)
print("t2 = ",t2)
print("t1+t2 = ",t_sum)
print("t1-t2 = ",t_diff)
print("t1*t2 = ",t_prod)
print("t1/t2 = ",t_div)
print("")
