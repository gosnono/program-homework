import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

rgb_list = [(255, 0, 0)]
one_px = np.array(rgb_list)[np.newaxis, :, :]

plt.imshow(np.array(one_px))
plt.axis('off')
plt.show()

