import pandas as pd

def load_data():
    df=pd.read_csv("stock_market_dataset.csv")
    return df
    
def clean_data(df):
    df = df.drop_duplicates()

    df = df.dropna()

    df["Date"]=pd.to_datetime(df["Date"])

    return df

def moving_average(df):
    df["MA7"]=df["Close"].rolling(7).mean()
    return df

def heighest_price(df):
    return df["High"].max()

def lowest_price(df):
    return df["Low"].min()