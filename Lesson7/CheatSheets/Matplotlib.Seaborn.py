# ============================
# Matplotlib & Seaborn Cheat Sheet
# Used for creating visualizations.
# ============================

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# ============================
# Matplotlib Basics
# ============================

# Simple Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Plotting Multiple Lines
y2 = np.cos(x)
plt.plot(x, y, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Multiple Line Plot')
plt.legend()
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()

# Bar Plot
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.bar(categories, values)
plt.title('Bar Plot')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Histogram')
plt.show()

# Pie Chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')
plt.show()

# ============================
# Customizing Matplotlib Plots
# ============================

# Adding Titles, Labels, and Legends
plt.plot(x, y)
plt.title('Title')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend(['sin(x)'])
plt.grid(True)  # Add grid
plt.show()

# Adjusting Figure Size and DPI
plt.figure(figsize=(8, 6), dpi=100)
plt.plot(x, y)
plt.show()

# Saving a Plot
plt.plot(x, y)
plt.savefig('plot.png')  # Save plot to a file

# Subplots
plt.subplot(2, 1, 1)  # (rows, cols, index)
plt.plot(x, y, 'r')
plt.title('First Plot')

plt.subplot(2, 1, 2)
plt.plot(x, y2, 'b')
plt.title('Second Plot')

plt.tight_layout()  # Prevent overlap
plt.show()

# ============================
# Seaborn Basics
# ============================

# Load a sample dataset
tips = sns.load_dataset('tips')

# Basic Scatter Plot with Seaborn
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Seaborn Scatter Plot')
plt.show()

# Line Plot
sns.lineplot(x='size', y='tip', data=tips)
plt.title('Seaborn Line Plot')
plt.show()

# Bar Plot
sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Seaborn Bar Plot')
plt.show()

# Count Plot (Bar plot for categorical data)
sns.countplot(x='day', data=tips)
plt.title('Seaborn Count Plot')
plt.show()

# ============================
# Seaborn Statistical Plots
# ============================

# Histogram (Distribution Plot)
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title('Seaborn Histogram with KDE')
plt.show()

# Box Plot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Seaborn Box Plot')
plt.show()

# Violin Plot (Combines Box Plot and KDE)
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Seaborn Violin Plot')
plt.show()

# Pairplot (Pairwise relationships)
sns.pairplot(tips)
plt.title('Seaborn Pairplot')
plt.show()

# ============================
# Seaborn Customization
# ============================

# Set styles
sns.set_style('whitegrid')  # Available styles: white, dark, whitegrid, darkgrid, ticks
sns.lineplot(x='size', y='tip', data=tips)
plt.title('Seaborn with Custom Style')
plt.show()

# Color Palettes
sns.set_palette('coolwarm')  # Other palettes: deep, muted, bright, pastel, dark, colorblind
sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Bar Plot with Custom Palette')
plt.show()

# ============================
# Combining Matplotlib & Seaborn
# ============================

# Seaborn enhances Matplotlib plots by adding better defaults
# You can combine both libraries

sns.set(style='whitegrid')
plt.figure(figsize=(10, 6))

# Seaborn scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)

# Customizing further with Matplotlib
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.grid(True)
plt.show()

# ============================
# End of Cheat Sheet
# ============================