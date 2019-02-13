#%%
from scipy import sparse
import numpy

data = numpy.ones(4)
row_indices = numpy.arange(4)
col_indices = numpy.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n{}".format(eye_coo))

#%%
from Ipython import display
