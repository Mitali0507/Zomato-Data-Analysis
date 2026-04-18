import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#creating dataframe
df=pd.read_csv("Zomato-data-.csv")
print(df.head(5))

#DATA CLEANING AND PREPARATION
#1.converting the rate column from string to float by removing denominator characters

def handleRate(value): #function that clean and convert each rating into float
    value=str(value).split('/')
    value=value[0]; #indicates the index number, eg:(4.1/5)=(4.1,/5), here [0]=4.1(value)
    return float(value)

df['rate']=df['rate'].apply(handleRate)
print(df.head())

#Identifying the most votes restaurant
max_votes=df['votes'].max()
restaurant_with_max_votes=df.loc[df['votes']==max_votes,"name"]
print('Restaurant(s) with max votes: ')
print(restaurant_with_max_votes)
