#%%
# numpy
from scipy import sparse
import numpy

x = numpy.array([[1, 2, 3], [4, 5, 6]])
print("x: \n{}".format(x))


#%%
# SciPy

# 対角成分が１でそれ以上が0の、２次元NumPy配列を作る
from scipy import sparse
import numpy
eye = numpy.eye(4)
print("NumPy array:\n{}".format(eye))

# Numpy配列をSciPyの形式のsparse matrixに変換して出力します。
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy space SCR matrix:\n{}".format(sparse_matrix))

#%%