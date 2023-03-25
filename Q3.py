import numpy as np
import matplotlib.pyplot as plt
from func import get_random_point,pla,pocket
import time

arr,pos_x,pos_y,neg_x,neg_y = get_random_point(2000)
start = time.time()
w,ct = pla(arr,pos_x,pos_y,neg_x,neg_y)
end = time.time()
print('PLA algorithm use ' + str(end - start) + ' seconds')
nx = np.arange(2000)
yd = (-w[1]/w[2])* nx - (w[0]/w[2])
plt.plot(pos_x,pos_y,'o',color='blue',markersize=2.0)
plt.plot(neg_x,neg_y,'o',color='red',markersize=2.0)
plt.plot(nx,yd,c='g',linewidth=0.5)
plt.show()
           
start = time.time()
w,ct = pocket(arr,pos_x,pos_y,neg_x,neg_y)
end = time.time()
print('Pocket algorithm use ' + str(end - start) + ' seconds')
nx = np.arange(2000)
yd = (-w[1]/w[2])* nx - (w[0]/w[2])
plt.plot(pos_x,pos_y,'o',color='blue',markersize=2.0)
plt.plot(neg_x,neg_y,'o',color='red',markersize=2.0)
plt.plot(nx,yd,c='g',linewidth=0.5)
plt.show()