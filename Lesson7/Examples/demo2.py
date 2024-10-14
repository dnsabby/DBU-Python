# Import libraries
import pandas as pd

# Sample dataset with missing values
data = {'Name': ['Tom', 'Nick', 'John', 'Peter'],
        'Age': [20, 21, None, 23],
        'Gender': ['M', 'M', 'M', None]}
df = pd.DataFrame(data)

# Display original data
print("Original Data:")
print(df)

# Handle missing values by filling with default values
df_cleaned = df.fillna({'Age': df['Age'].mean(), 'Gender': 'Unknown'})
print("\nCleaned Data:")
print(df_cleaned)