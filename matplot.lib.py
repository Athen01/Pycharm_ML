import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=6+3*np.sin(2*x)
fig,a=plt.subplots()
a.plot(x,y,linewidth=2.0)
a.set(xlim=(0,8),xticks=np.arange(1,8),
      ylim=(0,8),yticks=np.arange(1,8))
plt.show()