import random
import matplotlib.pyplot as plt

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
print(color)

plt.scatter(random.randint(0, 10), random.randint(0,10), c=color, s=200)
plt.show()
