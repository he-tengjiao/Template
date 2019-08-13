import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.io
import numpy as np
params={
    'font.family': 'times new roman',
    'axes.labelsize': '20',       
    'xtick.labelsize':'20',
    'ytick.labelsize':'20',
    'lines.linewidth': 3,
    'legend.fontsize': '17',
    'figure.figsize'   : '12, 9'    # set figure size
}
pylab.rcParams.update(params)            #set figure parameter
#line_styles=['ro-','b^-','gs-','ro--','b^--','gs--']  #set line style
 
 
 
         
#We give the coordinate date directly to give an example.
#x1 = [1,2,3,4,5]
y1 = [19.8978596*1000/30,13.5339078*1000/30,10.555486*1000/30,9.1540528*1000/30,7.0560222*1000/30] #MILP
y2 = [15.3155164*1000/30,9.22103226*1000/30,5.867776*1000/30,4.689652*1000/30,3.646047*1000/30] #Protocol
y3 = [12.3666206*1000/30,6.564300942*1000/30,2.105315026*1000/30,2.05715091*1000/30,0.49742151*1000/30]



 
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
width = 0.3
plt.bar(ind,y1,width,color = 'dimgray',edgecolor="black",label = 'MILP')  
plt.bar(ind+width,y2,width,color = 'silver',edgecolor="black",label = 'D-CFG') # ind+width adjusts the left start location of the bar.
plt.bar(ind+2*width,y3,width,color = 'white',edgecolor="black",label = 'COMP') 

for a, b in zip(x1, y1):
    plt.text(a, b + 0.01, '%.1f' % b, ha='center', va='bottom', fontsize=17)
    
for a, b in zip(x1, y2):
    plt.text(a+width, b + 0.01, '%.1f' % b, ha='center', va='bottom', fontsize=17)
    

for a, b in zip(x1, y3):
    plt.text(a+2*width, b + 0.01, '%.1f' % b, ha='center', va='bottom', fontsize=17)

plt.xticks(np.arange(5) + width, ('1','2','3','4','5'))

 
fig1 = plt.figure(1)
axes = plt.subplot(111)  
#axes = plt.gca()
#axes.set_yticks([0,2,4,6,8,10,12,14,16])
#axes.set_xticks([15,20,25,30,35])
#axes.grid(True)  # add grid
#axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6])
axes.set_axisbelow(True)
axes.grid(axis='y',linestyle='-.')  # add grid
 
plt.legend(loc="upper right")  #set legend location
plt.ylabel('Max-min rate (bits/s)')   # set ystick label
plt.xlabel('Number of sources')  # set xstck label
 
plt.savefig('Source.eps',dpi = 1000,bbox_inches='tight')
plt.show()