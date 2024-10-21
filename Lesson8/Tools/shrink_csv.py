import pandas as pd
import os

# Tool to help you shrink a XLS or CSV file down to a specified number of rows

# Set the working directory path to the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

fileName = os.getcwd() + '/OnlineRetail.xlsx'
outputFileName = os.getcwd() + '/OnlineRetail.csv'
rowSize = 2000

# Check if the file exists
if os.path.exists(fileName):
    df = pd.read_excel(fileName)

    # Get random rows from the file based on the rowSize
    if len(df) < rowSize:
        raise ValueError(f"The file {fileName} contains fewer than {rowSize} rows.")
    else:
        # Get random rows from the file based on the rowSize
        df = df.sample(n=rowSize)

        # Write the file back to csv disk
        df.to_csv(outputFileName, index=False)
else:
    raise ValueError(f"The file {fileName} does not exist.")