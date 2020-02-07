import numpy as np
a= np.random.randint(1,20,15)
print(a)
b= a.reshape(3,5)
print(b)
max_value = np.amax(b,axis=1)
print(max_value)
b=np.where(b == np.max(b,axis=1).reshape(-1,1),0,b)
print(b)