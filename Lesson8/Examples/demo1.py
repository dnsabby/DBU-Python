import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Download stock data from Yahoo Finance
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
stock_data = yf.download(tickers, start='2020-01-01', end='2023-01-01')['Adj Close']

# Calculate daily returns
returns = stock_data.pct_change().dropna()

# Simulate initial portfolio
weights = np.random.rand(len(tickers))
weights /= np.sum(weights)
portfolio = (returns * weights).sum(axis=1).cumsum()

# Plot with interactive portfolio weights adjustment
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)

# Initial plot
l, = ax.plot(portfolio.index, portfolio, label='Portfolio')

# Set labels and title with increased font size
ax.set_xlabel('Date', fontsize=14, fontweight='bold')
ax.set_ylabel('Cumulative Return', fontsize=14, fontweight='bold')
ax.set_title('Interactive Portfolio Cumulative Return', fontsize=16, fontweight='bold')

plt.grid(True)

# Create sliders for each stock's weight
sliders = []
for i, ticker in enumerate(tickers):
    ax_slider = plt.axes([0.1, 0.2 - i * 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, f'Weight {ticker}', 0, 1, valinit=weights[i])
    sliders.append(slider)

# Update function when sliders are adjusted
def update(val):
    # Retrieve the weights from the sliders
    new_weights = np.array([s.val for s in sliders])
    new_weights /= new_weights.sum()  # Normalize to ensure the weights sum to 1
    
    # Recalculate portfolio returns
    portfolio = (returns * new_weights).sum(axis=1).cumsum()
    
    # Update the plot
    l.set_ydata(portfolio)
    fig.canvas.draw_idle()

# Attach the update function to the sliders
for slider in sliders:
    slider.on_changed(update)

plt.show()