# ============================
# Scikit-learn Cheat Sheet
# Simple Machine learning algorithms.
# ============================

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris, load_boston
import pandas as pd

# ============================
# Loading Data
# ============================

# Sample datasets
iris = load_iris()  # Iris dataset
X, y = iris.data, iris.target

# Convert to DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ============================
# Preprocessing Data
# ============================

# Standardization (Scaling Features)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Label Encoding (Categorical -> Numerical)
encoder = LabelEncoder()
y_train_encoded = encoder.fit_transform(y_train)

# ============================
# Linear Regression
# ============================

# Fitting a linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Making predictions
y_pred = lin_reg.predict(X_test)

# Evaluating the model
print(f"R^2 score: {lin_reg.score(X_test, y_test)}")

# ============================
# Logistic Regression (Classification)
# ============================

# Fitting a logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

# Making predictions
y_pred_log_reg = log_reg.predict(X_test_scaled)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred_log_reg)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_log_reg)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_log_reg)}")

# ============================
# Support Vector Machine (SVM)
# ============================

# Fitting an SVM model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train_scaled, y_train)

# Making predictions
y_pred_svm = svm_model.predict(X_test_scaled)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred_svm)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_svm)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_svm)}")

# ============================
# Random Forest Classifier
# ============================

# Fitting a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Making predictions
y_pred_rf = rf_model.predict(X_test_scaled)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred_rf)
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_rf)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred_rf)}")

# ============================
# Model Evaluation
# ============================

# Confusion Matrix
print(confusion_matrix(y_test, y_pred))

# Accuracy Score
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Classification Report
print(classification_report(y_test, y_pred))

# ============================
# Cross-Validation
# ============================

from sklearn.model_selection import cross_val_score

# Perform cross-validation
scores = cross_val_score(RandomForestClassifier(), X, y, cv=5)  # 5-fold cross-validation
print(f"Cross-Validation Scores: {scores}")
print(f"Average Cross-Validation Score: {scores.mean()}")

# ============================
# Hyperparameter Tuning (GridSearchCV)
# ============================

from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}

# Set up GridSearchCV
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Best parameters
print(f"Best Parameters: {grid_search.best_params_}")

# ============================
# Feature Scaling (Standardization vs Normalization)
# ============================

# Standardization (zero mean, unit variance)
scaler = StandardScaler()
X_train_standardized = scaler.fit_transform(X_train)

# Normalization (scaling between 0 and 1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)

# ============================
# Dimensionality Reduction (PCA)
# ============================

from sklearn.decomposition import PCA

# Apply PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)

# Explained variance ratio
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")

# ============================
# End of Cheat Sheet
# ============================