import numpy as np
import random
import matplotlib.pyplot as plt
import time
# Q1
m,b=3,2
def get_random_point(num): # 亂數產生num筆資料，一半標1，一半標-1
  pos_x,pos_y = [],[]
  neg_x,neg_y = [],[]
  arr = []
  for _ in range(num//2):
    x = random.randint(0,num)
    r = random.randint(max(10,num//5),num)
    y = m*x + b - r
    pos_x.append(x)
    pos_y.append(y)
    arr.append([x,y,1])

  for _ in range(num//2):
    x = random.randint(0,num)
    r = random.randint(max(10,num//5),num)
    y = m*x + b + r

    neg_x.append(x)
    neg_y.append(y)
    arr.append([x,y,-1])
    
  return arr,pos_x,pos_y,neg_x,neg_y

# Q2
def check(w,arr,pos_x,pos_y,neg_x,neg_y,state): # 檢查有無分類錯誤, return [錯誤的點，錯誤的標記，錯誤幾個點]
    wrong_coor,wrong_label = None,None
    ct = 0 # count wrong times

    wrong_coor = []
    wrong_label = []
    for i,[x,y,l] in enumerate(arr):
        x = [x,y]
        c = np.concatenate((np.array([1.]),np.array(x)))
        if sign(np.dot(w,c)) != l:
            if state: # pla algo
                return c,l,1
            ct += 1
            wrong_coor.append(c)
            wrong_label.append(l)
    
    if ct == 0:
        return None,None,None
    else:
        idx = random.randint(0,len(wrong_coor)-1)
        return wrong_coor[idx],wrong_label[idx],ct
  
def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def pla(arr,pos_x,pos_y,neg_x,neg_y):
    w = np.zeros(3)
    ct = 0
    while True:
        x,s,wrong_times = check(w,arr,pos_x,pos_y,neg_x,neg_y,True)
        if x is None:
            break
        w += np.array(s)*x
        ct += 1 
    return w,ct

def pocket(arr,pos_x,pos_y,neg_x,neg_y,max_iteration = 500): # 最多跑max_iteration次，預設500
    m = {}
    w = np.zeros(3)
    ct = 0
    while max_iteration:
        x,s,wrong_times = check(w,arr,pos_x,pos_y,neg_x,neg_y,False)
        if x is None:
            break
        max_iteration -= 1
        m[tuple(w)] = wrong_times
        w += np.array(s)*x
        ct += 1
    if max_iteration > 0: # 若還沒跑到n次就已經沒錯誤了，代表有一條線能切開2邊
        return w,0
    
    mn_wrong = float('inf')
    mn_wrong_w = None
    for k,v in m.items():
        if v < mn_wrong:
            mn_wrong = v
            mn_wrong_w = k
    return mn_wrong_w,mn_wrong