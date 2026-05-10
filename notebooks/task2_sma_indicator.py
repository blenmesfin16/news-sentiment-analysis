import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

# Load AAPL data
aapl = pd.read_csv('../data/raw/AAPL.csv')
aapl['Date'] = pd.to_datetime(aapl['Date'])
aapl = aapl.sort_values('Date')

# Calculate SMAs
aapl['SMA_20'] = aapl['Close'].rolling(20).mean()
aapl['SMA_50'] = aapl['Close'].rolling(50).mean()

# Create plot
plt.figure(figsize=(12, 6))
plt.plot(aapl['Date'], aapl['Close'], label='Close Price', linewidth=1, color='black')
plt.plot(aapl['Date'], aapl['SMA_20'], label='SMA 20', linewidth=2, color='blue')
plt.plot(aapl['Date'], aapl['SMA_50'], label='SMA 50', linewidth=2, color='red')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('AAPL - Simple Moving Average (SMA) Technical Indicator')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot
plt.savefig('../plots/sma_indicator.png', dpi=150)
print("✅ SMA indicator saved to 'plots/sma_indicator.png'")

# Show the plot
plt.show()