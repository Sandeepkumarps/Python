import scipy.stats as stats
import numpy as np

data_group1=np.array([10 ,20,0,15,15,30,15,6,0,46,60,2,3,8,9,10])
data_group2=np.array([10,51,20 ,10,50,60,50,90,80,70,102,3,6,4])

print(np.var(data_group1),np.var(data_group2))
stats.ttest_ind(a=data_group1,b=data_group2,equal_var=True)