import numpy as np
def cal_mean(data,freq):
    return np.sum(data*freq)/np.sum(freq)
def cal_variance(data,freq):
    mean =cal_mean(data,freq)
    return np.sum(freq*(data-mean)**2)/np.sum(freq)
def std_dev(data,freq):
    return np.sqrt(cal_variance(data,freq))

data=np.array([10,20,30,40,50])
freq=np.array([5,10,15,10,5])

print(cal_mean(data,freq))
print(cal_variance(data,freq))
print(std_dev(data,freq))
