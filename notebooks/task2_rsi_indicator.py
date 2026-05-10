"""
TASK 2: RSI Technical Indicator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

print("="*60)
print("TASK 2: RSI TECHNICAL INDICATOR")
print("="*60)

# Load AAPL data
aapl = pd.read_csv('../data/raw/AAPL.csv')
aapl['Date'] = pd.to_datetime(aapl['Date'])
aapl = aapl.sort_values('Date')

def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

aapl['RSI_14'] = calculate_rsi(aapl['Close'])

# Latest values
latest_rsi = aapl['RSI_14'].iloc[-1]
print(f"\n📊 LATEST RSI (14-day): {latest_rsi:.1f}")

if latest_rsi > 70:
    signal = "OVERBOUGHT (SELL)"
elif latest_rsi < 30:
    signal = "OVERSOLD (BUY)"
else:
    signal = "NEUTRAL"

print(f"   Signal: {signal}")

# Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1])

ax1.plot(aapl['Date'], aapl['Close'], color='black', linewidth=1)
ax1.set_ylabel('Price ($)')
ax1.set_title('AAPL Stock Price')
ax1.grid(True, alpha=0.3)

ax2.plot(aapl['Date'], aapl['RSI_14'], color='purple', linewidth=1)
ax2.axhline(y=70, color='red', linestyle='--', label='Overbought (70)')
ax2.axhline(y=30, color='green', linestyle='--', label='Oversold (30)')
ax2.fill_between(aapl['Date'], 30, 70, alpha=0.1, color='gray')
ax2.set_ylabel('RSI')
ax2.set_xlabel('Date')
ax2.set_title('RSI (14-day)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../plots/rsi_indicator.png', dpi=150)
plt.show()

print("\n✅ RSI indicator saved to 'plots/rsi_indicator.png'")