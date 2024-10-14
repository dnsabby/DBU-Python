# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Simple bar plot using Matplotlib
categories = ['A', 'B', 'C']
values = [3, 7, 5]

plt.bar(categories, values)
plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()