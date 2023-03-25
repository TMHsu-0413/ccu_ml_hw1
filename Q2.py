import numpy as np
import matplotlib.pyplot as plt
from func import get_random_point,pla

sum = 0
for i in range(3):
    arr,pos_x,pos_y,neg_x,neg_y = get_random_point(30)
    w,ct = pla(arr,pos_x,pos_y,neg_x,neg_y)
    sum += ct
    print("random",i," use ",ct," times")
    nx = np.arange(30)
    yd = (-w[1]/w[2]) * nx - (w[0]/w[2])
    plt.plot(pos_x,pos_y,'o',color='blue',markersize=2.0)
    plt.plot(neg_x,neg_y,'o',color='red',markersize=2.0)
    plt.plot(nx,yd,c='g',linewidth=0.5)
    plt.show()

print("average ",sum//3," times")