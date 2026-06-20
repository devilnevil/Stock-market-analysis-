# 📈 Stock Market Data Analysis Pipeline

A modular Python-based data analysis tool designed to ingest, clean, and process historical stock market data. This project implements technical indicators like a **7-Day Moving Average (MA7)** and provides clean, customized visual charts using **Matplotlib**.

## 🚀 Project Overview

In quantitative finance and stock trading, everyday raw data is filled with duplicate entries, missing values, and high-frequency noise. This pipeline automates the data preprocessing steps and applies moving averages to filter out daily price fluctuations, helping analysts identify short-term market momentum.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3.10+
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib

---

## 📁 Project Structure

```text
├── analasyis.py          # Handles Data Loading, Data Cleaning, and Core Logic (MA7, Min/Max)
├── visualization.py      # Contains Matplotlib logic for plotting trends and customizing charts
├── main.py               # The Orchestrator / Entry point of the application
└── stock_market_dataset.csv  # Raw input data
