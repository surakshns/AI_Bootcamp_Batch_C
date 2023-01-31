from datetime import datetime, date

import numpy as np
from numpy import longdouble, int64
from numpy.compat import long

myarr = np.array([1,2,3,45,7])
#myarr = np.array([[1,2,3],[4,5,6]])
print(type(myarr))
print(myarr.dtype)
print(myarr.ndim)

print(np.sum(myarr))

myarr*=2
print(myarr)

#[111,'Rajesh',2016-12-25,5000]

dtypes = [('id',int),('name','<U9'),('Join_Date',date),('salary',int64)]
data = [(111,'Rajesh','2016-12-25',5000),(222,'Suraj','2016-12-25',70000000000)]

emparr = np.array(data,dtypes)
print(emparr)