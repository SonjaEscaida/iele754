import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

uniform_data = stats.uniform.rvs(size = 100000, loc = 0, scale= 10)

pd.DataFrame(uniform_data).plot(kind="density", figsize=(9,9), xlim=(-1,11))

stats.uniform.cdf(x=2.5, loc=0, scale=10)  #Al correrlo =0.25

stats.uniform.ppf(q=0.4, loc=0, scale=10) #= 4.0

for x in range (-1,12,3)
print("Density as x value"+ str(x))
print (stats.uniform.pdf(x, loc=0, scale=10))




