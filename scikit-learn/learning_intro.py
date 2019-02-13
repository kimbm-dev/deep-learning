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

# Numpy配列をSciPyの形式の疎行列(そぎょうれつ)に変換して出力します。
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy space SCR matrix:\n{}".format(sparse_matrix))

#%%
from scipy import sparse
import numpy

data = numpy.ones(4)
row_indices = numpy.arange(4)
col_indices = numpy.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n{}".format(eye_coo))

#%%
#%matplotlib inline
import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(-10, 50, 500)
y = numpy.sin(x)
plt.plot(x, y, marker="x")
