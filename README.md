# 📈 NASDAQ Wishlist Tracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A lightweight web app for tracking NASDAQ stocks with real-time technical indicators**

[Features](#-features) • [Quick Start](#-quick-start-google-colab) • [Local Setup](#-local-setup) • [Customization](#-customization)

</div>

---

## 🎯 Overview

Track your favorite NASDAQ stocks with real-time technical analysis including:
- 50 & 200-day Moving Averages
- RSI (14) indicators
- Buy/Sell/Hold signals
- 30-day price sparklines
- Distance from 52-week highs

Perfect for personal analysis, rapid prototyping, and learning technical indicators!

## ✨ Features

### Complete Technical Analysis Dashboard

| Column | Description |
|--------|-------------|
| **Company Name** | Full company name from Yahoo Finance |
| **Ticker** | Stock symbol |
| **Price ($)** | Current market price |
| **52W Range** | Annual high/low range |
| **SMA 50** | 50-day Simple Moving Average |
| **SMA 200** | 200-day Simple Moving Average |
| **RSI (14)** | 14-period Relative Strength Index |
| **Trend** | Bullish (SMA50 > SMA200) or Bearish |
| **Signal** | BUY/SELL/HOLD based on RSI |
| **30D Sparkline** | Visual 30-day price trend |
| **% Down from Top** | Distance from 52-week high |

### Smart Signal Logic
- 🟢 **BUY** - RSI < 30 (oversold condition)
- 🔴 **SELL** - RSI > 70 (overbought condition)
- ⚪ **HOLD** - RSI between 30-70 (neutral)

### Beautiful, Responsive UI
- Modern gradient design
- Interactive Chart.js sparklines
- Color-coded signals
- Mobile-friendly layout
- One-click refresh

## 🚀 Quick Start (Google Colab)

### Option 1: One-Command Launch

```python
# In a new Google Colab notebook, run:
!git clone https://github.com/YOUR_USERNAME/nasdaq-wishlist-tracker.git
%cd nasdaq-wishlist-tracker
!python run_colab.py
```

The script will:
1. ✅ Install all dependencies automatically
2. 🔑 Ask for your ngrok token (one-time setup)
3. 🌐 Generate a public URL
4. 🚀 Launch the app

### Option 2: With Environment Variable

```python
import os
os.environ['NGROK_AUTH_TOKEN'] = 'your_token_here'

!git clone https://github.com/YOUR_USERNAME/nasdaq-wishlist-tracker.git
%cd nasdaq-wishlist-tracker
!python run_colab.py
```

### Get Your ngrok Token (Free)
1. Sign up at [ngrok.com](https://ngrok.com/)
2. Get your auth token from [dashboard](https://dashboard.ngrok.com/get-started/your-authtoken)
3. Paste it when prompted (or set as environment variable)

---

## 💻 Local Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/nasdaq-wishlist-tracker.git
cd nasdaq-wishlist-tracker
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your ngrok token
```

4. **Run the app**
```bash
python run_colab.py
```

Or run Flask directly:
```bash
python app.py
```

Then open: `http://localhost:5000`

---

## ⚙️ Customization

### Modify Your Watchlist

Edit the `WATCHLIST` variable in `app.py`:

```python
WATCHLIST = [
    "AAPL",   # Apple
    "MSFT",   # Microsoft
    "NVDA",   # NVIDIA
    "GOOGL",  # Google
    "AMZN",   # Amazon
    "TSLA",   # Tesla
    "META",   # Meta
    "NFLX",   # Netflix
    "AMD",    # AMD
    "INTC"    # Intel
]
```

**Recommended:** Up to 50 stocks for optimal performance

### Customize Indicators

Modify indicator parameters in `app.py`:

```python
# Change SMA periods
sma_50 = hist_6m['Close'].rolling(window=50).mean()
sma_200 = hist_6m['Close'].rolling(window=200).mean()

# Change RSI period
rsi_series = ta.rsi(hist_6m['Close'], length=14)

# Customize signal thresholds
if rsi_14 < 30:  # Change oversold threshold
    signal = "BUY"
elif rsi_14 > 70:  # Change overbought threshold
    signal = "SELL"
```

---

## 📁 Project Structure

```
nasdaq-wishlist-tracker/
├── app.py                  # Flask backend & indicator logic
├── config.py               # Configuration settings
├── run_colab.py           # Google Colab launcher
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── templates/
│   └── index.html         # Frontend UI
├── COLAB_INSTRUCTIONS.txt # Quick Colab guide
└── README.md              # This file
```

---

## 🔧 Technical Stack

- **Backend:** Flask, Python 3.9+
- **Data Source:** Yahoo Finance (yfinance)
- **Indicators:** pandas-ta
- **Frontend:** HTML, Vanilla JavaScript, Chart.js
- **Tunnel:** ngrok (for Colab deployment)

---

## 📊 Performance

- **Max watchlist:** 50 stocks (recommended)
- **Initial load:** < 15 seconds
- **Per-ticker calculation:** < 500ms
- **Update frequency:** Manual refresh (on-demand)

---

## 🐛 Troubleshooting

### ngrok Connection Issues
```bash
# Verify your token is correct
echo $NGROK_AUTH_TOKEN

# Check ngrok status
ngrok version
```

### Data Not Loading
- ✅ Verify ticker symbols are valid NASDAQ stocks
- ✅ Check internet connection
- ✅ Ensure Yahoo Finance is accessible

### Indicators Show "N/A"
- Recent IPOs may lack 200-day history
- Delisted stocks won't have data
- Check if ticker is correct

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## 🎓 How It Works

### Indicator Calculations

**SMA (Simple Moving Average)**
- SMA 50: Average closing price over last 50 days
- SMA 200: Average closing price over last 200 days
- Golden Cross (Bullish): SMA50 crosses above SMA200
- Death Cross (Bearish): SMA50 crosses below SMA200

**RSI (Relative Strength Index)**
- Measures momentum on scale of 0-100
- < 30: Oversold (potential buy)
- > 70: Overbought (potential sell)
- 30-70: Neutral (hold)

**% Down from Top**
- Shows how far current price is from 52-week high
- Useful for identifying value opportunities
- Formula: `(52W_High - Current_Price) / 52W_High × 100`

---

## 🚧 Limitations

- No authentication system
- Session-based (no persistent storage)
- Manual refresh required
- Not for production trading
- No real-time streaming quotes
- Yahoo Finance API rate limits apply

---

## 🛣️ Roadmap

- [ ] CSV import/export for watchlists
- [ ] Sector grouping and filtering
- [ ] Sortable columns
- [ ] SQLite persistence
- [ ] Auto-refresh option
- [ ] Email/SMS alerts
- [ ] Portfolio tracking
- [ ] Historical backtesting

---

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) for market data
- [yfinance](https://github.com/ranaroussi/yfinance) for API wrapper
- [pandas-ta](https://github.com/twopirllc/pandas-ta) for technical indicators
- [Chart.js](https://www.chartjs.org/) for beautiful visualizations
- [ngrok](https://ngrok.com/) for easy tunneling

---

## 📧 Contact

Questions or suggestions? Open an issue or reach out!

---

<div align="center">

**⭐ If you find this helpful, please star the repo!**

Made with ❤️ for traders and developers

</div>
