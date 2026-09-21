import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/Computers H/Downloads/cafeteria_sales.csv')

#print(data.to_string())
#IDENTIFY AND HANDLING DATA
data["Transaction Date"].replace(["UNKNOWN","ERROR"],np.nan,inplace=True)
data["Item"].replace(["UNKNOWN","ERROR"],np.nan,inplace=True)
data["Quantity"].replace(["UNKNOWN","ERROR"],np.nan,inplace=True)
data["Price Per Unit"].replace(["UNKNOWN","ERROR"],np.nan,inplace=True)

#print(data.to_string())


#FILLING MISSING VALUES
mo=data["Item"].mode()[0]
data["Item"].fillna(mo,inplace=True)
#print(data)

mo=data["Quantity"].mode()[0]
data["Quantity"].fillna(mo,inplace=True)
#print(data)
mo=data["Price Per Unit"].mode()[0]
data["Price Per Unit"].fillna(mo,inplace=True)
#print(data)
print(data.to_string())


#CONVERT DATATYPES
data['Transaction Date'] = pd.to_datetime(data['Transaction Date'], errors='coerce')
print(data["Transaction Date"])


data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce').astype('Int64')
print(data['Quantity'])

data['Price Per Unit']=pd.to_numeric(data['Price Per Unit'],errors='coerce')
print(data['Price Per Unit'])



#REMOVE DUPLICATES


data.drop_duplicates(inplace=True)
#print(data.duplicated())
data.dropna(inplace=True)
print(data.info())

#CORRELATION

print(data.corr(numeric_only=True))

#PLOT-BAR GRAPH
df=data["Item"].value_counts()
df.plot(kind='bar')
plt.show()

#CLEAN
data.to_csv('C:/Users/Computers H/Downloads/cafeteria_sales_clean.csv')



