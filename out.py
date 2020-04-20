import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,10)
y=x**2

fig=plt.figure()

axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes1.set_title("plot")
axes1.plot(x,y,label='x sqaure',color='orange')
axes1.plot(y,x,label='x cube')

axes1.legend()



fig.savefig('myplot.png')
plt.show()

