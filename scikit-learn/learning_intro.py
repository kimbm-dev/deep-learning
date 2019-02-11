# %%
# numpy
from scipy import sparse
import numpy

x = numpy.array([[1, 2, 3], [4, 5, 6]])
print("x: \n{}".format(x))


# %%
# SciPy

# 対角成分が１でそれ以上が0の、２次元NumPy配列を作る
eye = numpy.eye(4)
print("NumPy array:\n{}".format(eye))
