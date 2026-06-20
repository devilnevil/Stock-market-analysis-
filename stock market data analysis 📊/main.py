from analasyis import load_data, clean_data, moving_average, heighest_price, lowest_price
from visualization import plot_chart


df = load_data()
print(df.head())

df = clean_data(df)
print(df)

df = moving_average(df)
print(df.head(10))

hig_val = heighest_price(df)
print("Highest price = ", hig_val)

low_val = lowest_price(df)
print("Lowest Price = ", low_val)

plot_chart(df)
