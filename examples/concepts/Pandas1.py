import pandas as pd

data = [(555,'Kai','2016-12-25',5000),(222,'Aman','2016-12-25',700)]

df = pd.DataFrame(data)
#print(df)

stdf1 = pd.read_csv('C:/Development/AI_Bootcamp_Batch_C/data/student.csv',header=None)
print(stdf1)

stdf2 = pd.read_csv('C:/Development/AI_Bootcamp_Batch_C/data/student.csv',names=['id','name','grade'])
print(stdf2)