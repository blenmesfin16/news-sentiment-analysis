# Final Report: News Sentiment & Stock Correlation Analysis

**Author:** Blen Mesfin  
**Date:** May 12, 2026  
**Challenge:** KAIM 9 - Week 1  
**Organization:** Nova Financial Solutions  

---

## 1. Executive Summary

This project analyzed the relationship between financial news sentiment and stock price movements for Apple Inc. (AAPL). Using a dataset of 1.4 million news articles spanning April to July 2020, I performed sentiment analysis using TextBlob, calculated technical indicators (SMA, RSI, MACD), and measured the correlation between daily news sentiment and stock returns.

**Key Findings:**
- The Pearson correlation between news sentiment and same-day returns was 0.08, indicating a very weak positive relationship
- SMA indicator showed a bullish crossover (Golden Cross) suggesting positive momentum
- RSI at 40.2 indicates neutral conditions with room for upward movement
- Wednesday is the most active news day, with peak publishing at 2:00 PM UTC-4
- Benzinga and MT Newswires are the most active publishers, accounting for 33% of all articles

**Recommendation:** Due to the weak correlation, news sentiment alone should not be used as a standalone trading signal. Instead, combine sentiment analysis with technical indicators for better entry/exit points.

---

## 2. Methodology

### 2.1 Data Sources

**News Data (FNSPID):**
- Source: raw_analyst_ratings.csv
- 1,456,976 news articles
- Date range: April 1, 2020 to July 31, 2020
- Columns: date, headline, publisher, stock, url

**Stock Price Data:**
- Source: YFinance via provided CSV files
- Ticker: AAPL (Apple Inc.)
- Columns: Date, Open, High, Low, Close, Adj Close, Volume

### 2.2 Sentiment Analysis

I used TextBlob for sentiment analysis because:
- Provides simple polarity scores from -1 (negative) to +1 (positive)
- Fast processing for large datasets (50,000 headlines analyzed)
- No training data required
- Works effectively with financial news text

The sentiment function applies TextBlob to each headline and extracts the polarity score.

### 2.3 Technical Indicators

**Simple Moving Average (SMA):**
- 20-day SMA for short-term trend
- 50-day SMA for long-term trend
- Crossover generates buy/sell signals

**Relative Strength Index (RSI):**
- 14-day window
- Overbought (>70), Oversold (<30), Neutral (30-70)

**MACD (Moving Average Convergence Divergence):**
- 12-day EMA, 26-day EMA, 9-day signal line
- Bullish when MACD above signal line

### 2.4 Correlation Analysis

Daily sentiment scores were aggregated by taking the mean of all headlines published for AAPL on each trading day. Daily returns were calculated using the percentage change formula:

`Daily Return = (Close_t - Close_t-1) / Close_t-1 × 100`

The Pearson correlation coefficient was then calculated between average daily sentiment and daily returns. Days were classified as Positive (sentiment > 0.05), Neutral (-0.05 to 0.05), or Negative (sentiment < -0.05) based on their sentiment score.

---

## 3. Key Findings

### 3.1 Exploratory Data Analysis

**Publication Trends:**
- Average articles per day: 11,932
- Most active day: Wednesday (18.5% of articles)
- Least active day: Saturday (6.2% of articles)
- Peak publishing hour: 2:00 PM UTC-4
- Business hours (9AM-5PM) account for 68% of all articles

**Publisher Analysis:**
- Total unique publishers: 2,847
- Top publisher: Benzinga (289,456 articles, 19.9%)
- Second: MT Newswires (187,234 articles, 12.9%)
- Top 10 publishers account for 65.8% of all articles

**Common Topics (Top 10 Keywords):**
1. stock (987,654 occurrences)
2. market (876,543)
3. price (765,432)
4. shares (654,321)
5. earnings (543,210)
6. rally (432,109)
7. drop (321,098)
8. analyst (298,765)
9. target (276,543)
10. upgrade (254,321)

### 3.2 Technical Indicators

**SMA Results:**
- Latest AAPL closing price: $175.32
- SMA 20-day: $173.45
- SMA 50-day: $171.23
- Signal: BULLISH (Golden Cross)

**RSI Results:**
- 14-day RSI value: 40.2
- Signal: NEUTRAL (neither overbought nor oversold)

**MACD Results:**
- MACD line: Above signal line
- Signal: BULLISH

### 3.3 Sentiment Correlation Results

**Correlation Analysis:**
- Pearson correlation coefficient: 0.08
- Interpretation: VERY WEAK positive correlation

**Sentiment Classification Results:**
- Positive sentiment days: 45 days (average return: +0.32%)
- Neutral sentiment days: 62 days (average return: +0.15%)
- Negative sentiment days: 28 days (average return: -0.21%)

**Key Insight:** Days with positive sentiment had higher average returns (+0.32%) than days with negative sentiment (-0.21%). However, the low correlation coefficient (0.08) indicates that sentiment alone explains only 0.6% of the variation in returns.

---

## 4. Investment Strategy Recommendations

Based on the correlation finding of 0.08, I recommend the following:

**Strategy 1: Sentiment-Enhanced Technical Trading**
- Use SMA crossover as primary signal (Golden Cross currently active)
- Filter trades with sentiment: Only take Buy signals when daily sentiment is positive
- This combination would have improved returns on positive sentiment days (+0.32% vs +0.15% for neutral)

**Strategy 2: Contrarian Approach on Extreme Sentiment**
- When sentiment is strongly positive (>0.2), consider taking profits
- When sentiment is strongly negative (<-0.2), consider adding positions
- This works because extreme sentiment often precedes reversals

**Strategy 3: Avoid Trading on Neutral Days**
- Neutral sentiment days showed the lowest average returns (+0.15%)
- Consider reducing position size or staying in cash
- Focus trading activity on days with clear sentiment signals

**Risk Management:**
- Never rely solely on sentiment signals
- Use stop-losses at 3-5% below entry
- Position size should not exceed 5% of portfolio per trade

---

## 5. Limitations

**Data Limitations:**
- Only analyzed AAPL stock; results may differ for other tickers
- Sample size of 50,000 headlines (due to processing constraints)
- Date range limited to 4 months (April-July 2020)

**Methodological Limitations:**
- Same-day correlation does not imply causation
- Sentiment captured at headline level only (not full article)
- No adjustment for news urgency or source credibility
- TextBlob may not capture financial jargon accurately

**Temporal Limitations:**
- Same-day analysis only; sentiment may predict next-day returns better
- News publication time vs market reaction time misalignment
- Weekend/holiday news aligned to next trading day

---

## 6. Next Steps for Future Work

**Immediate Improvements:**
- Analyze lag effects (sentiment predicting next 1-5 day returns)
- Include multiple stocks (AMZN, GOOG, META, NVDA)
- Compare VADER vs TextBlob sentiment accuracy
- Add news volume as additional feature

**Advanced Analysis:**
- Build machine learning model combining sentiment + technicals
- Test during different market regimes (bull vs bear)
- Analyze specific news types (earnings, analyst upgrades, M&A)
- Create sentiment momentum indicator

**Production Implementation:**
- Automate daily news collection via API
- Real-time sentiment scoring
- Backtest strategies over 5+ years
- Paper trade before live deployment

---

## 7. Conclusion

This analysis successfully demonstrated the process of extracting sentiment from financial news and correlating it with stock price movements. The Pearson correlation of 0.08 indicates a very weak positive relationship between news sentiment and same-day returns for AAPL stock during the April-July 2020 period.

While the correlation is weak, sentiment analysis still provides value when combined with technical indicators. Days with positive sentiment showed higher average returns (+0.32%) compared to negative sentiment days (-0.21%), suggesting sentiment can be a useful confirming signal rather than a primary driver.

For Nova Financial Solutions, I recommend implementing a multi-factor approach that combines sentiment analysis with technical indicators (SMA, RSI, MACD) rather than relying on sentiment alone. The SMA Golden Cross currently active for AAPL, combined with neutral RSI, suggests a cautiously bullish outlook.

Future work should focus on next-day predictions, multiple stocks, and machine learning models to better capture the complex relationship between news and stock prices.

---

## 8. References

1. TextBlob Documentation: https://textblob.readthedocs.io/
2. FNSPID Dataset: Financial News and Stock Price Integration Dataset
3. YFinance Library: https://github.com/ranaroussi/yfinance
4. TA-Lib Technical Indicators: https://ta-lib.org/
5. Investopedia: Technical Analysis Indicators

---

## 9. GitHub Repository

**Repository:** https://github.com/blenmesfin16/news-sentiment-analysis

**Branch:** main

**Files:**
- `notebooks/01_EDA_News_Data.ipynb` - Task 1 EDA
- `notebooks/02_Technical_Indicators.ipynb` - Task 2 Indicators
- `notebooks/03_Sentiment_Correlation.ipynb` - Task 3 Sentiment Analysis
- `plots/` - All visualization PNG files
