from datetime import datetime, date

import numpy as np
from numpy import longdouble, int64
from numpy.compat import long

#myarr = np.array([1,2,3,45,7])
myarr = np.array([[11,20,3],[40,5,6]])
print(type(myarr))
print(myarr.dtype)
print(myarr.ndim)

print(np.sum(myarr))
#print(np.sort(myarr,axis=0)) for column
print(np.sort(myarr,axis=None))

myarr*=2
#print(myarr)

#[111,'Rajesh',2016-12-25,5000]

dtypes = [('id',int),('name','<U9'),('Join_Date',date),('salary',int64)]
data = [(555,'Kai','2016-12-25',5000),(222,'Aman','2016-12-25',700)]

emparr = np.array(data,dtypes)
print(np.sort(emparr,order=('name','salary')))