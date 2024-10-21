import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create a simple dataset with random data
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'z': np.random.randn(100)
})

# add a column with a color label
data['color'] = np.where(data['z']>0, 'green', 'red')

# create a figure and axis
fig, ax = plt.subplots()
ax.scatter(data['x'], data['y'], c=data['color'])

# add a regression line throughout the data
z = np.polyfit(data['x'], data['y'], 1)
p = np.poly1d(z)
ax.plot(data['x'], p(data['x']), "black")

# set labels and title
ax.set_title('Scatter plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

# show plot
plt.show()





