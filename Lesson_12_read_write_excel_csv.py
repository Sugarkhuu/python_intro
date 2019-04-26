# Sources
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
#https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.dropna.html
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html

import os
os.chdir("C:/Users/Sugar2/Documents/py/Python intro")

import pandas as pd

# Read excel
df = pd.read_excel('myfile.xlsx')
df = pd.read_excel('myfile.xlsx', sheet_name='data')
df = pd.read_excel('myfile.xlsx', sheet_name= 1)
df = pd.read_excel('myfile.xlsx', sheet_name='data', index_col=0)
df = pd.read_excel('myfile.xlsx', sheet_name=1, index_col=1)
df = pd.read_excel('myfile.xlsx', sheet_name=1, index_col=1, header=1)
df = pd.read_excel('myfile.xlsx', sheet_name=1, usecols = "B,C:D")
df = pd.read_excel('myfile.xlsx', sheet_name=1, skiprows= 3, index_col=0)
df = pd.read_excel('myfile.xlsx', sheet_name=1, header=[0,1,2,3])
#multiple header
df['Name', 'Bat']

# Read CSV
df = pd.read_csv('myfile.csv',sep=',')
df = pd.read_csv('myfile.csv',sep=',', header=[0,1,2])
df = pd.read_csv('myfile.csv',sep=',', header=[0,1,2], index_col=0)


# Read txt, json
cf = pd.read_csv('myfile.txt',sep=',')
cf = pd.read_csv('myfile.json',sep=',')


# Write to CSV and excel
df.to_csv('maf.csv')
df.to_csv('maf.csv', sep=';')
df.to_excel('maf.xlsx', sheet_name='myData')


#handle NaN
df.dropna(how='all', axis=1)
df.dropna(axis=0, how = 'any')
df.fillna(0)
df.fillna(method='bfill')
df.fillna(method='ffill')
df.fillna(method='ffill', axis=0)
df.interpolate(method='linear')
df.interpolate(method='polynomial', order=2)
df.interpolate(method='spline', order=2)


# Next time: Read, MANIPULATE and write to excel

## Packages

#xlrd
#openpyxl
#xlwings
#csv
