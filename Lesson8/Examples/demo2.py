import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import os

# Load the dataset
os.chdir(os.path.dirname(os.path.abspath(__file__)))
customer_df = pd.read_csv('../Tools/OnlineRetail.csv', encoding='ISO-8859-1')

# Basic preprocessing
customer_df = customer_df.dropna(subset=['CustomerID'])  # Drop rows with missing customer data
customer_df['Spending'] = customer_df['Quantity'] * customer_df['UnitPrice']  # Calculate total spending
customer_summary = customer_df.groupby('CustomerID').agg({'Spending': 'sum', 'InvoiceNo': 'nunique'})
customer_summary.rename(columns={'InvoiceNo': 'Frequency'}, inplace=True)

# Normalize data (Standardizing feature scales)
# ------------------------------------------------
# When features like 'Spending' and 'Frequency' have different ranges,
# normalization ensures that they contribute equally to the analysis. 
# We use StandardScaler here to scale the data so that each feature
# has a mean of 0 and a standard deviation of 1. 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
customer_summary_scaled = scaler.fit_transform(customer_summary)

# K-Means clustering (Clustering the data)
# ------------------------------------------------
# K-Means is a type of unsupervised learning used to identify groups 
# or clusters in data. In this case, we are segmenting customers 
# into different clusters based on their 'Spending' and 'Frequency' 
# patterns. The algorithm tries to minimize the variance within each 
# cluster, so similar customers are grouped together.
kmeans = KMeans(n_clusters=3)  # We start with 3 clusters
customer_summary['Cluster'] = kmeans.fit_predict(customer_summary_scaled)

# Interactive clustering plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

# Scatter plot
scat = ax.scatter(customer_summary['Spending'], customer_summary['Frequency'], c=customer_summary['Cluster'], cmap='viridis')
ax.set_xlabel('Spending', fontsize=14, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=14, fontweight='bold')
ax.set_title('Customer Segmentation', fontsize=16, fontweight='bold')

# Add slider for changing the number of clusters
ax_cluster = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_cluster = Slider(ax_cluster, 'Clusters', 2, 10, valinit=3, valstep=1)

# Update function for slider interaction
def update(val):
    k = int(slider_cluster.val)
    
    # K-Means clustering for dynamic cluster updates
    # ------------------------------------------------
    # Here, we're using the K-Means algorithm to allow the user 
    # to interactively adjust the number of clusters, dynamically 
    # reassigning customers to new clusters based on their 'Spending' 
    # and 'Frequency'.
    kmeans = KMeans(n_clusters=k)
    customer_summary['Cluster'] = kmeans.fit_predict(customer_summary_scaled)
    
    # Update scatter plot data
    scat.set_offsets(customer_summary[['Spending', 'Frequency']])
    scat.set_array(customer_summary['Cluster'])
    fig.canvas.draw_idle()

# Attach slider to the update function
slider_cluster.on_changed(update)

# Add colorbar for cluster visualization
plt.colorbar(scat, ax=ax)
plt.show()