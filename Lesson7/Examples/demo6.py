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

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['sepal length (cm)']], df['sepal width (cm)'], test_size=0.2)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Output the Test Data
print("Test Data Set:")
print(X_test)

# Make predictions
predictions = model.predict(X_test)

# Print predictions
print("Predictions on test data:")
print(predictions)