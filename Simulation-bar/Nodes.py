# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 07:34:07 2019

@author: Steven
"""

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.io
import numpy as np
params={
    'font.family': 'times new roman',
    'axes.labelsize': '23',       
    'xtick.labelsize':'23',
    'ytick.labelsize':'23',
    'lines.linewidth': 3,
    'legend.fontsize': '18',
    'figure.figsize'   : '12, 9'    # set figure size
}
pylab.rcParams.update(params)            #set figure parameter
#line_styles=['ro-','b^-','gs-','ro--','b^--','gs--']  #set line style
 
 
 
         
#We give the coordinate date directly to give an example.
#x1 = [15,20,25,30,35]
y1 = [13.48257/30,13.22102/30,13.4838072/30,13.844593/30,13.9415996/30] #MILP
y2 = [7.434513/30,6.786522/30,8.870274/30,7.204962/30,8.5032902/30] #Protocol
y3 = [4.529566/30,4.4692321/30,5.46453046/30,4.264338078/30,4.49825362/30]







'''
plt.plot(x1,y1,'ro-',label='MILP',markersize=20) # in 'bo-', b is blue, o is O marker, - is solid line and so on
plt.plot(x1,y2,'bv-',label='D-CFG',markersize=20)
'''

'''
p1= plt.errorbar(x1,y1,yerr=[errL1,errU1],capsize=6, capthick=2,ecolor='r',fmt='-o',color='r')
p2= plt.errorbar(x1,y2,yerr=[errL2,errU2],capsize=6, capthick=2,ecolor='b',fmt='-v',color='b')
'''
#p11 = plt.bar(range(len(x1)), y1,bottom=stacked,color='b',edgecolor="black",linewidth ="1")


x1 = range(5)
ind = np.arange(5)                # the x locations for the groups
width = 0.28
plt.bar(ind,y1,width,color = 'dimgray',edgecolor="black",label = 'MILP')  
plt.bar(ind+width,y2,width,color = 'silver',edgecolor="black",label = 'D-CFG') # ind+width adjusts the left start location of the bar.
plt.bar(ind+2*width,y3,width,color = 'white',edgecolor="black",label = 'COMP') 

for a, b in zip(x1, y1):
    plt.text(a, b + 0.01, '%.2f' % b, ha='center', va='bottom', fontsize=17)
    
for a, b in zip(x1, y2):
    plt.text(a+width, b + 0.01, '%.2f' % b, ha='center', va='bottom', fontsize=17)
    

for a, b in zip(x1, y3):
    plt.text(a+2*width, b + 0.01, '%.2f' % b, ha='center', va='bottom', fontsize=17)

plt.xticks(np.arange(5) + width, ('15','20','25','30','35'))

 
fig1 = plt.figure(1)
axes = plt.subplot(111)  
#axes = plt.gca()
#axes.set_yticks([0,2,4,6,8,10,12,14,16,18])
#axes.set_xticks([15,20,25,30,35])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6])
#axes.grid(axis='y',linestyle='-.')  # add grid
 
plt.legend(loc="upper left")  #set legend location
plt.ylabel('Max-min rate (kbps)')   # set ystick label
plt.xlabel('Number of nodes')  # set xstck label
 
plt.savefig('Node.eps',dpi = 1000,bbox_inches='tight')
plt.grid()
plt.show()