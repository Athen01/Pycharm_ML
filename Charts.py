import matplotlib.pyplot as plt
import numpy as np
x=np.array(["karnataka","ap","tn","tg"])
y=np.array([68,55,61,34])
plt.bar(x,y)
plt.show()
plt.pie(y)
plt.show()