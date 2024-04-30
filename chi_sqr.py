import scipy.stats as stats
import numpy as np

observed_data=[15 ,34,30,10,11,7]
expected_data=[4,29,25,30,2,5]

chi_square_test_statistic,p_value=stats.chisquare(observed_data,expected_data)
print(chi_square_test_statistic)
print(p_value)