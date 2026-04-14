
# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- CLI input using argparse
- Input validation
- Logging of API requests and errors
- Structured modular code

## Project Structure

<pre>
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
└── README.md
</pre>
## Setup

Clone the repository:

git clone <repo_url>

Navigate to project:

cd trading_bot

Install dependencies:

pip install -r requirements.txt

Create a `.env` file:

BINANCE_API_KEY=your_api_key <br>
BINANCE_API_SECRET=your_api_secret

## Usage

Example MARKET order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Example LIMIT order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000

## Logging

Logs are saved in:

bot.log

## Assumptions

- Binance Futures Testnet account is required
- Only USDT-M futures symbols are supported
EOF
