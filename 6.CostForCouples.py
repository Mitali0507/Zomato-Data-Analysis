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

#analysing the approx cost for two people to find preferred price range
couple_data=df["approx_cost(for two people)"]
sns.countplot(x=couple_data)
plt.savefig("preferred price for couples")
plt.show()
