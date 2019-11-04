import numpy as np
# from numba import vectorize
from numba import jit
from parallelo import DimensaoMatrixError
@jit(nopython=True)
def mul_cuda(obj, other):
    return obj * other
@jit(nopython=True)
def soma_cuda(obj):
    return np.sum(obj)
class MatrixMulCuda(np.ndarray):   
    def __new__(cls, array):
        obj = array.view(cls)
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        if not isinstance(obj, np.ndarray):
            raise "A matrix deve ser do tipo array: np.ndarray"
        self.obj = obj
        self.info = getattr(obj, 'info', None)  
    def __str__(self):
        texto = np.array2string(self.obj, separator=',')
        return ''.join(texto.splitlines())

    def __mul__(self, other):
        if isinstance(other, (np.ndarray, self.__class__)):
            return self.mul_matrix(other)
        elif isinstance(other, (np.int, np.int8, np.int16, np.int32, np.int_)):
            return self.mul_scalar(other)
        else:
            raise "A operação deve ser relizada por uma matriz ou um vetor"  
    def mul_scalar(self, other):
        rows, cols = self.obj.shape
        C = np.zeros((rows, cols))
        for j in range(cols):
            col = self.obj[:,[j]]
            C[:,[j]] = col * other
        return C
    def mul_matrix(self, other):
        rows, k, m = self.obj.shape[0], self.obj.shape[1], other.shape[1]
        if not k == other.shape[0]:
            raise DimensaoMatrixError(self.obj.shape, other.shape)
        C = np.zeros((rows, m))
        for ii in range(rows):
            for jj in range(m):
                aa = self.obj[ii,:]
                bb = other[:,jj]
                C[ii,jj] = soma_cuda(mul_cuda(aa,bb))
import numpy as np
# from numba import vectorize
from numba import jit
from parallelo import DimensaoMatrixError
@jit(nopython=True)
def mul_cuda(obj, other):
    return obj * other
@jit(nopython=True)
def soma_cuda(obj):
    return np.sum(obj)
class MatrixMulCuda(np.ndarray):   
    def __new__(cls, array):
        obj = array.view(cls)
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        if not isinstance(obj, np.ndarray):
            raise "A matrix deve ser do tipo array: np.ndarray"
        self.obj = obj
        self.info = getattr(obj, 'info', None)  
    def __str__(self):
        texto = np.array2string(self.obj, separator=',')
        return ''.join(texto.splitlines())

    def __mul__(self, other):
        if isinstance(other, (np.ndarray, self.__class__)):
            return self.mul_matrix(other)
        elif isinstance(other, (np.int, np.int8, np.int16, np.int32, np.int_)):
            return self.mul_scalar(other)
        else:
            raise "A operação deve ser relizada por uma matriz ou um vetor"  
    def mul_scalar(self, other):
        rows, cols = self.obj.shape
        C = np.zeros((rows, cols))
        for j in range(cols):
            col = self.obj[:,[j]]
            C[:,[j]] = col * other
        return C
    def mul_matrix(self, other):
        rows, k, m = self.obj.shape[0], self.obj.shape[1], other.shape[1]
        if not k == other.shape[0]:
            raise DimensaoMatrixError(self.obj.shape, other.shape)
        C = np.zeros((rows, m))
        for ii in range(rows):
            for jj in range(m):
                aa = self.obj[ii,:]
                bb = other[:,jj]
                C[ii,jj] = soma_cuda(mul_cuda(aa,bb))
        return C