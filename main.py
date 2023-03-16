from BinarySearch import binarySearch as jana

import numpy as np

x=jana(np.arange(20,101),100)
y = x.search_inside()
x.verify(y)
