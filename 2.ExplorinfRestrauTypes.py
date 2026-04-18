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
print(df.head(5))

#EXPLORING RESTAURANT TYPES
#1. Using listed_in(type) to check out popular restaurant categories using countplot
sns.countplot(x=df['listed_in(type)'])
plt.xlabel('Type of Restaurant')
plt.savefig('Type of Restaurant') 
plt.show()

''' This plot shows that Dining and cafes are quite popular, majority falls in Dining
'''

#2.Votes by Restaurant
grouped_data=df.groupby('listed_in(type)')['votes'].sum() #calculates individual votes by each category
result=pd.DataFrame({'votes':grouped_data}) #making a new Df
plt.plot(result, c='blue',marker='*')
plt.xlabel("Type of Retaurant")
plt.ylabel('Votes')
plt.savefig('Votes by category')
plt.show()

'''Dining restaurants are preferred by larger number of people'''