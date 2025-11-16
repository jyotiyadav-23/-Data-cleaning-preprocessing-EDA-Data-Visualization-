import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"E:\Internship\Sentiment dataset.csv")
df
df.head()
df.info()
df.drop_duplicates()
df.duplicated()
df['Timestamp']=pd.to_datetime(df['Timestamp'],errors='coerce')
df['Timestamp']
df['Likes'].mean()
df['Likes'].std()
df['Country'].mode()
df['Retweets'].mean()
df1=pd.read_csv(r"E:\Internship\churn-bigml-80.csv")
df1
df1.head(10)
df1.info()
df1['International plan'].mode()
df1['Customer service calls'].mean()
df1['Churn'].mode()
df1['Total intl calls'].sum()
df1['Total day charge'].mean()
df1['Total night calls'].sum()
df1.head(10)
plt.figure(figsize=(8,6))
sns.boxplot(x='Total intl calls',y='Total day calls',data=df1, color='red')
plt.show()
plt.figure(figsize=(20,10))
sns.scatterplot(x='State', y='Number vmail messages', data=df1,color='blue', marker='D')
plt.show()
plt.figure(figsize=(8,6))
sns.histplot(x='Account length', discrete=False,hue='International plan',palette='spring',data=df1, kde=True)
plt.ylabel("International Plan")
plt.show()
df2=pd.read_csv(r"E:\Internship\Stock Prices Data Set.csv")
df2
corr=df2.corr()
corr
sns.heatmap(corr,annot=True, cmap='coolwarm')
plt.show()
df3=pd.read_csv(r"E:\Internship\Churan-bigml20.csv")
df3
plt.figure(figsize=(15,8))
sns.barplot(x='State',y='Customer service calls',hue='Churn',data=df3)
plt.legend(title='Churn')
plt.title('Simple Bar Plot')
plt.xlabel('State')
plt.ylabel('No. of Customer service calls')
plt.show()
plt.figure(figsize=(8,5))
sns.lineplot(x='Area code', y='Total intl charge', hue='International plan',data=df3)
plt.legend(title='International plan')
plt.xlabel('Area code')
plt.ylabel('Total No. of International charge')
plt.show()
df3.head(5)
plt.figure(figsize=(15,5))
sns.scatterplot(x='Total day calls', y='Customer service calls', data=df3, marker='^', color='purple')
plt.xlabel('Sum of day calls')
plt.ylabel('No. of customer service calls')
plt.show()












