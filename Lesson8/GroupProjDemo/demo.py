# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import os

# Load the dataset
# Make sure the dataset is in the same directory or provide the full path to the dataset
os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv('user_behavior_dataset.csv')

# 1. Data Exploration
# Display the first few rows of the dataset to get an overview
print("First 5 rows of the dataset:\n", df.head())

# Display summary statistics for numerical columns
print("\nSummary statistics:\n", df.describe())

# Check for missing values in the dataset
print("\nMissing values:\n", df.isnull().sum())

# 2. Data Visualization: Correlation heatmap
# Visualize the correlation between numerical variables using a heatmap
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Visualization: Distribution of App Usage Time based on User Behavior Class
# This helps to understand how app usage varies between different user behavior classes
plt.figure(figsize=(8, 6))
sns.boxplot(x='User Behavior Class', y='App Usage Time (min/day)', data=df)
plt.title('App Usage Time Distribution by User Behavior Class')
plt.show()

# 3. Data Preprocessing
# Convert categorical columns (Operating System, Gender) into numeric values using Label Encoding
le = LabelEncoder()
df['Operating System'] = le.fit_transform(df['Operating System'])
df['Gender'] = le.fit_transform(df['Gender'])

# Define features (X) and target (y)
# Features will include all columns except 'User ID', 'Device Model', and 'User Behavior Class'
X = df.drop(columns=['User ID', 'Device Model', 'User Behavior Class'])
y = df['User Behavior Class']

# Split the data into training and test sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling: Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Machine Learning: Logistic Regression Model
# Create and train the Logistic Regression model on the training data
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluation of the model's performance using confusion matrix and classification report
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualize Confusion Matrix using a heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()