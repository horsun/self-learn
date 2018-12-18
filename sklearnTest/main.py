import matplotlib
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import sklearn

data_bli = pd.read_csv("./bli.csv", thousands=',')
data_gdp = pd.read_csv("./gdp.csv", na_values="n/a")
X = np.mat(data_gdp[data_gdp['Year'] == 2015])
country_list = data_gdp[data_gdp['Year'] == 2015]['Country Name']
print(country_list.values)
print(data_bli[data_bli['Country'] in country_list.values])
# Y = np.mat(data_bli['Value'])
# plt.scatter(X, Y, color='green')
# plt.xlabel('year')
# plt.ylabel('statisfy')
# plt.title('first')
# plt.show()
