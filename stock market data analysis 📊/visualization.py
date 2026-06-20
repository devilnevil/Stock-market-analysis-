import matplotlib.pyplot as plt


def plot_chart(df):
    plt.figure(figsize=(12, 6))

    # close price plot
    plt.plot(df['Date'], df['Close'], label='Actual close price',
             color='#1f77b4', alpha=0.7, linestyle='-')

    # 7 Day moving average
    plt.plot(df['Date'], df['MA7'], label='7-DAY moving average',
             color='#ff7f0e', linewidth=2.5)

    # graph customs
    plt.title('Stock market analysis:Close price vs 7Day moving average',
              fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Date', fontsize=12, labelpad=10)

    # label adjustment padding pre-set
    plt.legend(loc='upper left', fontsize=11)

    # layout agdjustment padding pre-sets
    plt.tight_layout()

    # graph pop-up
    plt.show()

    
