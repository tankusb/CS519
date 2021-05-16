import numpy as np
from matplotlib import pyplot

a = np.array([(1,2),(3,4),(4,5), (4,3), (2,1)]).transpose()
b = np.array([(5,2),(8,4),(6,5), (8,3), (7,1)]).transpose()


pyplot.axis([0, 10, 0, 10])
pyplot.plot(a[0], a[1], "ro")
pyplot.plot(b[0], b[1], "bo")
pyplot.show()
