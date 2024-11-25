import math
#import matplotlib.pyplot as plt
import numpy as np

def f1(A,x,to):
    return (A+0.2)*((math.pi)/2+math.atan(math.log((x*to)+0.1)))/math.pi

def Speed_translation_tab_maker(speed_stat,acceleration_stat):
    Speed_translation_tab = []
    Speed = 0
    speed_max = speed_stat/10
    epsilon = 0.05
    i = 0
    accelerating = acceleration_stat/200
    while speed_max - Speed > epsilon:
        Speed = f1(speed_max,i,accelerating)
        Speed_translation_tab.append(Speed)
        i+=1
    Speed_translation_tab[0] = 0
    return Speed_translation_tab

Speed_tab= Speed_translation_tab_maker(5.5,8)
ind = [i for i in range(len(Speed_tab))]
Speed_tab_complete = []
ind_complete = []
t = 0
while f1(5.5/10,t,8/200) < Speed_tab[-1]:
    Speed_tab_complete.append(f1(5.5/10,t,8/200))
    ind_complete.append(t)
    t+=0.2

#print(Speed_tab)
"""
plt.plot(ind, Speed_tab, 'bo', ind_complete, Speed_tab_complete, 'r')
plt.show()"""
