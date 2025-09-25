import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import seaborn as sns

def Marvellousadvertise(Datapath):
    df = pd.read_csv(Datapath)
    
    print("Dataset sample is:")
    print(df.head())

    print("Clean the dataset")

    df.drop(columns= ["Unnamed: 0"],inplace=True)

    print("Updated dataset is :")

    print(df.head())

    print("Missing values in eah columns :",df.isnull().sum())

    print("statistical summary :",df.describe())  #describe method is use for statistical data

    print("Correlation matrix")
    print(df.corr())

def main():
    Marvellousadvertise("Advertising.csv")


if __name__=="__main__":
    main()


    