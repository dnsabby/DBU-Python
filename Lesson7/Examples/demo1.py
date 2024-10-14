# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Basic demonstration of library usage
# NumPy example
print("NumPy Array:")
array = np.array([1, 2, 3, 4])
print(array)

# Pandas DataFrame example
print("\nPandas DataFrame:")
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

# Matplotlib example (simple line plot)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Simple Line Plot")
plt.show()