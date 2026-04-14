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

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md

## Setup

Clone the repository:

git clone <repo_url>

Navigate to project:

cd trading_bot

Install dependencies:

pip install -r requirements.txt

Create `.env` file:

BINANCE_API_KEY=your_api_key  
BINANCE_API_SECRET=your_api_secret

## Usage

MARKET order example:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT order example:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000

## Logging

Logs are stored in:

bot.log

## Assumptions

- Binance Futures Testnet account is required
- Only USDT-M futures symbols are supported