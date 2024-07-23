import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def Read_From_Csv(csv_path):
    Stock_df = pd.read_csv(csv_path)
    return Stock_df

def Plot_graph(stock_df,catagory = "All"):

    if catagory == "All":
      plt.plot(stock_df["Open"])
      plt.plot(stock_df["High"])
      plt.plot(stock_df["Low"])
      plt.plot(stock_df["Close"])
    else:
        plt.plot(stock_df[catagory])

    plt.xlabel(stock_df["Date"])
    plt.ylabel(np.array([100,150,200,250,300,350,400]))
    plt.title("Tata Motors stock Price")
    plt.show()


if __name__ == "__main__":
    stock_df = Read_From_Csv("archive\TATAMOTORS_BSE_01Oct20-01Oct21.csv")
    Plot_graph(stock_df, input())
    

