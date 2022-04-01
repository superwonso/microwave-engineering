# Draw r=2,x=9 circle on Smith Chart
import numpy as np
from matplotlib import pyplot as plt


def SmithChart(ax,Smith='Z'):
    ax.set_aspect('equal', 'datalim') 
    ax.spines["right"].set_color("none")  
    ax.spines["top"].set_color("none")  
    ax.spines["left"].set_color("none")  
    ax.spines["bottom"].set_color("none")  
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.tick_params(color='none') 
    t=np.linspace(0,2*np.pi,100) 
    x=np.cos(t)
    y=np.sin(t)
    ax.plot(x,y,color='black',linewidth=2)
    x0=np.linspace(-1,1,10) 
    y0=np.zeros(10)
    ax.plot(x0,y0,'k',linewidth=1)
    k=[.2] 
    """for i in range(0,len(k)):
        x1=k[i]+(1 - k[i])*np.cos(t)
        y1=(1 - k[i]) * np.sin(t)
        if(Smith=='Z'):
            ax.plot(x1,y1,'k',lw=0.5)
        if(Smith=='Y'):
            ax.plot(-x1,-y1,'r',lw=0.5)"""
    kt=[-9]
    k2 = [-.5]
    for i in range(0,len(kt)):
        t = np.linspace(kt[i], 1.5*np.pi, 50) 
        a = 1 + k2[i] * np.cos(t)
        b = k2[i] + k2[i] * np.sin(t)
        if(Smith=='Z'):
            #ax.plot(a, b,'k',lw=0.5)
            ax.plot(a, -b,'k',lw=0.5)
        if(Smith=='Y'):
            #ax.plot(-a, b,'r:',lw=0.5)
            ax.plot(-a, -b,'r:',lw=0.5)
    
    return 0

fig = plt.figure(figsize=(20,5))
ax1 = 2
ax1 = fig.add_subplot(1,3,1)
SmithChart(ax1)

plt.show()