# Dataframe (Pandas) basics
# copy vs =
# inplace = True

import pandas as pd  # data manipulation analysis library of Python
import numpy as np   # computing library 
import matplotlib.pyplot as plt # plotting

############################################ BASIC

# Create a Series

s = pd.Series([1,3,5,np.nan,6,8])

# Create DF from a Numpy array
dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# Create DF from dictionaries
df2 = pd.DataFrame({'A' : 1., 
                    'B' : pd.Timestamp('20130102'), 
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

# Types of columns
df2.dtypes

# Using TAB in IPython Console
#df2.<TAB>

# Simplest DF
dfS=pd.DataFrame({'A': 100, 'B': 250})  # Error
dfS=pd.DataFrame({'A': 100, 'B': 250}, index=[0])

############################################ VIEW DATA

df.head()   # Top (default = 5)
df.tail()   # Bottom (default = 5)

df.index    # The index series
df.columns  # Column Names
df.values   # Just values

df.describe() # quick descriptive stat

df.T        # Transpose data

# Sort
df.sort_index(axis=0, ascending=False) # inplace=True for a permanent change
df.sort_values(by='B')


############################################ SELECTION

# Getting
df.A
df['A']
df[['A','B']]
df[0:3]

df['20130102':'20130104']

# Selection by Label
df.loc[dates[0]]
df.loc[dates[0],['A','B']]
df.loc['20130102',['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc[:,['A','B']]

# Access single value
df.at[dates[0],'A']

# Selection by Position
df.iloc[3]      # 3rd row
df.iloc[3:5,0:2] 
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]
df.iloc[1,1]

# Access single value
df.iat[1,1]

############################################ CONDITIONAL SELECTION 

df[df.A > 0]
df[(df.A > -1.5) & (df.A<1) & (df.C>0)]
df[(df.A < -.5) | (df.A>0.3)]
df2[df2.E=='test']

df[df > 0] # Boolean

# isin filter
df2 = df
df2 = df.copy()

df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]


# Setting

# New column from a series
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df['F'] = s1

# Set values by label and position
df.at[dates[0],'A'] = 0
df.iat[0,1] = 0

# new col by np assign
df.loc[:,'D'] = np.array([5] * len(df))

# Revert to negative
df2 = df.copy() ### diff = and copy
df2[df2 > 0] = -df2

############################################ MISSING DATA 

# np.nan
df.iloc[2,3]=np.nan

df.dropna(how='any') # drop all rows and columns with NaN
df.dropna(0,how='any') # drop all rows with NaN
df.dropna(1,how='any') # drop all rows with NaN
pd.isna(df)

# filling ... (interpolate)
df.fillna(value=5)

############################################ OPERATIONS

# Pay attention to the missing
df.mean()
df.mean(1)
df.sum()
df.count()

df.apply(np.cumsum)
df.apply(lambda x: x.count())
df.apply(lambda x: x.cumprod())
df.apply(lambda x: x.max() - x.min())

### Histogram

s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

# String
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()
s.str.find('a')
s.str.replace('a','y')

### Merge and concatenate (join similar)
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

left = pd.DataFrame({'key': ['faa', 'fee'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'faa'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
pd.merge(left, right, on='key',how='outer')

# Append

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
df.append(s, ignore_index=True)


######### Grouping

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})

df.groupby('A').sum()
df.groupby(['A','B']).sum()



# =============================================================================
# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
#                      'foo', 'foo', 'qux', 'qux'],
#                     ['one', 'two', 'one', 'two',
#                      'one', 'two', 'one', 'two']]))
# 
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# 
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# df2 = df[:4]
# 
# stacked = df2.stack()
# stacked.unstack()
# stacked.unstack(1)
# stacked.unstack(0)
# 
# =============================================================================


# Pivot Table

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'],aggfunc='count') # Dem by changing

### Time series

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample('1Min').sum()
ts.resample('30S').mean()
ts.resample('25S').count()

# =============================================================================
# rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
# ts = pd.Series(np.random.randn(len(rng)), rng)
# 
# ts_utc = ts.tz_localize('UTC')
# ts_utc.tz_convert('US/Eastern')
# 
# rng = pd.date_range('1/1/2012', periods=5, freq='M')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# 
# ps = ts.to_period()
# ps.to_timestamp()
# 
# prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
# ts = pd.Series(np.random.randn(len(prng)), prng)
# ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
# ts.head()
# 
# df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
# df["grade"] = df["raw_grade"].astype("category")
# df["grade"].cat.categories = ["very good", "good", "very bad"]
# df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
# df.sort_values(by="grade")
# df.groupby("grade").size()
# =============================================================================

#### PLOTTING
np.random.seed(123456)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()

plt.figure(); df.plot(); plt.legend(loc='best')

### SAVE AND LOAD

df.to_csv('foo.csv')
df = pd.read_csv('foo.csv')

df.to_excel('foo.xlsx', sheet_name='Sheet1')
df=pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

df.to_pickle('last_data')
df = pd.read_pickle('historical_data')
