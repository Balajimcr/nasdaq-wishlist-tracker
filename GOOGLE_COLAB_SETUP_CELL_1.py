"""
🚀 NASDAQ WISHLIST TRACKER - COMPLETE GOOGLE COLAB SETUP
========================================================

INSTRUCTIONS:
1. Run this cell first to create all files
2. Get your ngrok token from: https://dashboard.ngrok.com/get-started/your-authtoken
3. Run the LAUNCH cell below

"""

import os

# Create templates directory
os.makedirs('templates', exist_ok=True)

# ===== CREATE APP.PY =====
app_code = """from flask import Flask, render_template, jsonify
import yfinance as yf
import pandas as pd
import pandas_ta as ta

app = Flask(__name__)

# 🎯 CUSTOMIZE YOUR WATCHLIST HERE
WATCHLIST = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "AMD", "INTC"]

def get_company_name(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return info.get('longName', ticker)
    except:
        return ticker

def calculate_indicators(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist_1y = stock.history(period="1y")
        hist_6m = stock.history(period="6mo")

        if hist_1y.empty or hist_6m.empty:
            return None

        current_price = hist_1y['Close'].iloc[-1]
        week_52_high = hist_1y['High'].max()
        week_52_low = hist_1y['Low'].min()
        week_52_range = f"${week_52_low:.2f} - ${week_52_high:.2f}"

        sma_50 = hist_6m['Close'].rolling(window=50).mean().iloc[-1]
        sma_200 = hist_6m['Close'].rolling(window=200).mean().iloc[-1]

        rsi_series = ta.rsi(hist_6m['Close'], length=14)
        rsi_14 = rsi_series.iloc[-1] if not rsi_series.empty else None

        if pd.notna(sma_50) and pd.notna(sma_200):
            trend = "Bullish" if sma_50 > sma_200 else "Bearish"
        else:
            trend = "N/A"

        if pd.notna(rsi_14):
            if rsi_14 < 30:
                signal = "BUY"
            elif rsi_14 > 70:
                signal = "SELL"
            else:
                signal = "HOLD"
        else:
            signal = "N/A"

        pct_down = ((week_52_high - current_price) / week_52_high) * 100
        sparkline_data = hist_6m['Close'].tail(30).tolist()
        company_name = get_company_name(ticker)

        return {
            'company_name': company_name,
            'ticker': ticker,
            'price': round(current_price, 2),
            'week_52_range': week_52_range,
            'sma_50': round(sma_50, 2) if pd.notna(sma_50) else 'N/A',
            'sma_200': round(sma_200, 2) if pd.notna(sma_200) else 'N/A',
            'rsi_14': round(rsi_14, 2) if pd.notna(rsi_14) else 'N/A',
            'trend': trend,
            'signal': signal,
            'sparkline': sparkline_data,
            'pct_down': round(pct_down, 2)
        }
    except Exception as e:
        print(f"Error processing {ticker}: {str(e)}")
        return {
            'company_name': ticker, 'ticker': ticker, 'price': 'N/A',
            'week_52_range': 'N/A', 'sma_50': 'N/A', 'sma_200': 'N/A',
            'rsi_14': 'N/A', 'trend': 'N/A', 'signal': 'N/A',
            'sparkline': [], 'pct_down': 'N/A'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/watchlist')
def get_watchlist_data():
    results = []
    for ticker in WATCHLIST:
        print(f"Processing {ticker}...")
        data = calculate_indicators(ticker)
        if data:
            results.append(data)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
"""

with open('app.py', 'w') as f:
    f.write(app_code)

print("✅ app.py created")
