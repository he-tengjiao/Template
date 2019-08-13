import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.io
import numpy as np
params={
    'font.family': 'times new roman',
    'axes.labelsize': '20',       
    'xtick.labelsize':'20',
    'ytick.labelsize':'20',
    'lines.linewidth': 2,
    'legend.fontsize': '18',
    'figure.figsize'   : '16, 9'    # set figure size
}
pylab.rcParams.update(params)            #set figure parameter
#line_styles=['ro-','b^-','gs-','ro--','b^--','gs--']  #set line style
 
 
 
         
#We give the coordinate date directly to give an example.
x1 = [5,10,15,20,25,30,35,40,45,50]
y1 = [65.450544*1000/250,39.170732*1000/250,26.161936*1000/250,18.9184262*1000/250,13.826873*1000/250,11.7331062*1000/250,8.6617436*1000/250,6.3619544*1000/250,5.7349584*1000/250,4.102180934*1000/250] #MILP
y2 = [62.896258*1000/250,33.0996042*1000/250,16.3168452*1000/250,12.8616893*1000/250,8.30740078*1000/250,6.1504215*1000/250,4.282340535*1000/250,2.920271512*1000/250,1.73980436*1000/250,1.710775038*1000/250] #Protocol



'''
y1max = [71.9698,23.5706,24.9605,17.6921,13.6575]
y1min = [9.94343,9.26979,7.7219,7.39486,6.95539]


errL1 = []
errU1 = []
for i in range(5):
    errL1.append(y1max[i] - y1[i])
    errU1.append(y1[i] - y1min[i])


y2max = [63.3546,16.8386,15.691,11.9262,8.91996]
y2min = [4.47216,2.97392,1.3692,2.1615,1.18137]

errL2 = []
errU2 = []
for i in range(5):
    errL2.append(y2max[i] - y2[i])
    errU2.append(y2[i] - y2min[i])
'''


plt.plot(x1,y1,'o-',label='D-CFG',color='black',markersize=15) # in 'bo-', b is blue, o is O marker, - is solid line and so on
plt.plot(x1,y2,'v--',label='COMP',color='black',markersize=15)

'''
p1= plt.errorbar(x1,y1,yerr=[errL1,errU1],capsize=6, capthick=2,ecolor='r',fmt='-o',color='r')
p2= plt.errorbar(x1,y2,yerr=[errL2,errU2],capsize=6, capthick=2,ecolor='b',fmt='-v',color='b')
'''
#p11 = plt.bar(range(len(x1)), y1,bottom=stacked,color='b',edgecolor="black",linewidth ="1")

'''
x1 = [5,10,15,20,25,30,35,40,45,50]               # the x locations for the groups
width = 0.3
#plt.bar(ind,y1,width,color = 'white',edgecolor="black",label = 'MILP')  
#plt.bar(ind+width,y2,width,color = 'white',edgecolor="black",label = 'D-CFG', hatch="\\\\\\\\") # ind+width adjusts the left start location of the bar.
'''
for a, b in zip(x1, y1):
    plt.text(a+1, b+1, '%.1f' % b, ha='center', va='bottom', fontsize=15)
    
for a, b in zip(x1, y2):
    plt.text(a-1, b-1, '%.1f' % b, ha='center', va='bottom', fontsize=15)

plt.xticks(np.arange(10) + 0.5*width, ('5','10','15','20','25','30','35','40','45','50'))


 
fig1 = plt.figure(1)
axes = plt.subplot(111)  
#axes = plt.gca()
#axes.set_yticks([0,2,4,6,8,10,12,14,16])
axes.set_xticks([5,10,15,20,25,30,35,40,45,50])
axes.set_axisbelow(True)
axes.grid(linestyle='-.')  # add grid

 
plt.legend(loc="upper right")  #set legend location
plt.ylabel('Max-min rate (bits/s)')   # set ystick label
plt.xlabel('Number of sources')  # set xstck label
 
plt.savefig('L_Source.eps',dpi = 1000,bbox_inches='tight')
plt.show()