import numpy as np
import matplotlib.pyplot as plt
from func import get_random_point,pocket
import random

arr,pos_x,pos_y,neg_x,neg_y = get_random_point(2000)
max_iteration = 2000

w,wrong_coor = pocket(arr,pos_x,pos_y,neg_x,neg_y,max_iteration)
nx = np.arange(max_iteration)
yd = (-w[1]/w[2])* nx - (w[0]/w[2])
print(f"accuracy before mislabel : {(max_iteration-wrong_coor)/max_iteration * 100}%")
for x,y,l in arr:
    if l == 1:
        plt.plot(x,y,'o',color='blue',markersize=2.0)
    else:
        plt.plot(x,y,'o',color='red',markersize=2.0)
        
plt.plot(nx,yd,c='g',linewidth=0.5)
plt.show()

pos_idx = [random.randint(0,1000) for _ in range(50)]
neg_idx = [random.randint(1000,2000) for _ in range(50)]

for el in pos_idx: # 亂數產生50筆正數idx 並把label改-1
    arr[el][2] = -1
    
for el in neg_idx:# 亂數產生50筆負數idx 並把label改1
    arr[el][2] = 1


w,wrong_coor = pocket(arr,pos_x,pos_y,neg_x,neg_y,max_iteration)
nx = np.arange(max_iteration)
yd = (-w[1]/w[2])* nx - (w[0]/w[2])
print(f"accuracy after mislabel : {(max_iteration-wrong_coor)/max_iteration * 100}%")
for x,y,l in arr:
    if l == 1:
        plt.plot(x,y,'o',color='blue',markersize=2.0)
    else:
        plt.plot(x,y,'o',color='red',markersize=2.0)
        
plt.plot(nx,yd,c='g',linewidth=0.5)
plt.show()