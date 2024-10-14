# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load a dataset
from sklearn.datasets import load_iris
iris = load_iris()

# Convert to a Pandas DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Using Seaborn for a more complex visualization
sns.pairplot(df)
plt.show()