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
x1 = [50,100,150,200,250,300,350,400,450,500]
y1 = [1.093834562*1000/50,5.09383104*1000/100,9.9515802*1000/150,17.4667106*1000/200,22.91933*1000/250,29.437264*1000/300,36.933096*1000/350,42.28157*1000/400,51.274018*1000/450,55.734664*1000/500] #MILP
y2 = [0.053754928*1000/50,1.054620802*1000/100,5.007042529*1000/150,8.07500122*1000/200,15.2925548*1000/250,13.94023572*1000/300,28.801258*1000/350,26.5017*1000/400,42.718506*1000/450,44.012776*1000/500] #Protocol

'''
y1max = [2.6479,10.0143,19.0131,24.2895,33.6688,42.7792,49.6081,62.1249,64.1103,80.006]
y1min = [0,0,3.82425,8.69233,13.0875,19.7553,20.8079,30.3247,33.6514,33.9699]


errL1 = []
errU1 = []
for i in range(10):
    errL1.append(y1max[i] - y1[i])
    errU1.append(y1[i] - y1min[i])


y2max = [1.17702,5.09643,17.3822,22.8222,34.0377,33.5727,60.8548,64,66.7291,73.7748]
y2min = [0,0,0,0,2.83856,0.765856,3.13173,0.70192,12.032,15.4069]

errL2 = []
errU2 = []
for i in range(10):
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
x1 = [50,100,150,200,250,300,350,400,450,500]

ind = np.arange(5)                # the x locations for the groups
width = 0.3
plt.bar(ind,y1,width,color = 'white',edgecolor="black",label = 'MILP')  
plt.bar(ind+width,y2,width,color = 'white',edgecolor="black",label = 'D-CFG', hatch="\\\\\\\\") # ind+width adjusts the left start location of the bar.

for a, b in zip(x1, y1):
    plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=17)
    
for a, b in zip(x1, y2):
    plt.text(a+width, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=17)

plt.xticks(np.arange(5) + 0.5*width, ('10','20','30','40','50'))


'''
for a, b in zip(x1, y1):
    plt.text(a, b+2, '%.1f' % b, ha='center', va='bottom', fontsize=17)
    
for a, b in zip(x1, y2):
    plt.text(a, b+2, '%.1f' % b, ha='center', va='bottom', fontsize=17)

plt.xticks(np.arange(10) + 0.5*width, ('50','100','150','200','250','300','350','400','450','500'))


 
fig1 = plt.figure(1)
axes = plt.subplot(111)  
#axes = plt.gca()
#axes.set_yticks([0,20,40,60,80,100,120])
axes.set_xticks([50,100,150,200,250,300,350,400,450,500])
axes.grid(linestyle='-.')


plt.legend(loc="upper left")  #set legend location
plt.ylabel('Max-min rate (bits/s)')   # set ystick label
plt.xlabel('Number of slots')  # set xstck label
 
plt.savefig('L_Slot.eps',dpi = 1000,bbox_inches='tight')
plt.show()