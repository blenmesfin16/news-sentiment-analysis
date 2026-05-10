import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

# Load AAPL data
aapl = pd.read_csv('../data/raw/AAPL.csv')
aapl['Date'] = pd.to_datetime(aapl['Date'])
aapl = aapl.sort_values('Date')

# Calculate MACD
ema12 = aapl['Close'].ewm(span=12, adjust=False).mean()
ema26 = aapl['Close'].ewm(span=26, adjust=False).mean()
aapl['MACD'] = ema12 - ema26
aapl['Signal'] = aapl['MACD'].ewm(span=9, adjust=False).mean()
aapl['Histogram'] = aapl['MACD'] - aapl['Signal']

# Create plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1])

ax1.plot(aapl['Date'], aapl['Close'], color='black', linewidth=1)
ax1.set_ylabel('Price ($)')
ax1.set_title('AAPL Stock Price')
ax1.grid(True, alpha=0.3)

ax2.plot(aapl['Date'], aapl['MACD'], label='MACD', color='blue', linewidth=1)
ax2.plot(aapl['Date'], aapl['Signal'], label='Signal', color='red', linewidth=1)
ax2.bar(aapl['Date'], aapl['Histogram'], color='gray', alpha=0.3, label='Histogram')
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax2.set_xlabel('Date')
ax2.set_ylabel('MACD')
ax2.set_title('MACD Indicator')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../plots/macd_indicator.png', dpi=150)
plt.show()

print("✅ MACD indicator saved to 'plots/macd_indicator.png'")