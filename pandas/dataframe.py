import pandas as pd
import numpy as np
a=[10,20,30]
a1=pd.DataFrame(a)
print(a1)

ser=pd.Series()
print("Pandas series:", ser)
data=np.array(['G','a','y','a','t','r','i'])
ser=pd.Series(data)
print("Pandas series:\n",ser)