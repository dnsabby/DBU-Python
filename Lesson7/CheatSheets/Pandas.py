# ===================
# Pandas Cheat Sheet
# Provides data structures like DataFrames, making data manipulation easy.
# ===================

import pandas as pd

# ===================
# Creating DataFrames
# ===================

# From a dictionary
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data)

# From a list of lists
data = [[1, 2], [3, 4]]
df = pd.DataFrame(data, columns=['col1', 'col2'])

# From a CSV file
df = pd.read_csv('file.csv')

# From a dictionary with index
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data, index=['row1', 'row2'])

# ===================
# Viewing and Inspecting Data
# ===================

df.head()  # First 5 rows
df.tail()  # Last 5 rows
df.shape  # Rows and columns (rows, columns)
df.info()  # Summary of DataFrame
df.describe()  # Statistical summary
df.columns  # Column names
df.index  # Row labels (index)

# ===================
# Selecting Data
# ===================

# Selecting a column
df['col1']  # Single column (returns a Series)
df[['col1', 'col2']]  # Multiple columns (returns a DataFrame)

# Selecting rows by index
df.loc['row1']  # Select row by label
df.iloc[0]  # Select row by index position

# Selecting rows and columns
df.loc['row1', 'col1']  # Select specific row and column by label
df.iloc[0, 0]  # Select specific row and column by position

# Slicing rows
df.loc['row1':'row2']  # Slice rows by label
df.iloc[0:2]  # Slice rows by position

# Filtering rows
df[df['col1'] > 1]  # Filter rows based on column condition

# ===================
# Adding and Dropping Data
# ===================

# Adding a new column
df['new_col'] = [5, 6]  # Add column with new values

# Dropping a column
df.drop('col1', axis=1, inplace=True)  # Drop column by name

# Dropping a row
df.drop('row1', axis=0, inplace=True)  # Drop row by label

# Resetting index
df.reset_index(drop=True, inplace=True)  # Reset index and remove old index

# ===================
# Sorting Data
# ===================

df.sort_values('col1', ascending=True, inplace=True)  # Sort by column values
df.sort_index(ascending=False, inplace=True)  # Sort by index

# ===================
# Handling Missing Data
# ===================

df.isnull()  # Check for missing values
df.dropna()  # Drop rows with missing values
df.fillna(0)  # Fill missing values with 0

# Fill missing values with the column mean
df['col1'].fillna(df['col1'].mean(), inplace=True)

# ===================
# Data Aggregation
# ===================

df['col1'].sum()  # Sum of a column
df['col1'].mean()  # Mean of a column
df['col1'].min()  # Minimum of a column
df['col1'].max()  # Maximum of a column
df['col1'].count()  # Count non-NA/null entries of a column

# Grouping data
df_grouped = df.groupby('col1').sum()  # Group by column and sum
df_grouped = df.groupby('col1').agg({'col2': 'mean'})  # Group by column and apply aggregation

# ===================
# Merging and Joining DataFrames
# ===================

# Merging on a key column
df1 = pd.DataFrame({'key': ['A', 'B'], 'col1': [1, 2]})
df2 = pd.DataFrame({'key': ['A', 'B'], 'col2': [3, 4]})
df_merged = pd.merge(df1, df2, on='key')

# Joining by index
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
df_joined = df1.join(df2)

# Concatenating DataFrames
df_concat = pd.concat([df1, df2], axis=1)  # Concatenate along columns
df_concat = pd.concat([df1, df2], axis=0)  # Concatenate along rows

# ===================
# Apply and Lambda Functions
# ===================

# Applying a function to a column
df['col1'] = df['col1'].apply(lambda x: x + 1)  # Increment each value by 1

# Applying a function to a row
df['sum_col'] = df.apply(lambda row: row['col1'] + row['col2'], axis=1)

# ===================
# Working with Dates
# ===================

# Convert a column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract year, month, day, etc.
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# ===================
# Exporting Data
# ===================

df.to_csv('output.csv', index=False)  # Export DataFrame to CSV

df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)  # Export DataFrame to Excel

# ===================
# Pivot Tables
# ===================

# Create a pivot table
pivot = df.pivot_table(values='col1', index='col2', columns='col3', aggfunc='sum')

# ===================
# End of Cheat Sheet
# ===================