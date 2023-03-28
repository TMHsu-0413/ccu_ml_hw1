import numpy as np
import matplotlib.pyplot as plt
from func import get_random_point,m,b


arr,pos_x,pos_y,neg_x,neg_y = get_random_point(30)
nx = np.arange(30)
plt.plot(pos_x,pos_y,'o',color='blue',markersize=2.0)
plt.plot(neg_x,neg_y,'o',color='red',markersize=2.0)
yd = [(m*x+b) for x in nx]
plt.plot(nx,yd,c='g',linewidth=0.5)
plt.show()