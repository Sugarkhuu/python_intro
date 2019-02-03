# =============================================================================
# Pandas visualization and image processing basics
# =============================================================================


# Source
# [1] https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
# [2] https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
# [3] https://matplotlib.org/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data

df = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD')).cumsum()


# pyplot 
plt.plot(df['A'],df['B'])



# pandas starts
df.plot(x='A', y='B')
df.plot()
df.A.plot()
df[['A','B']].iloc[1:5].plot()


# Types of plots

df.iloc[5].plot(kind='bar')
df.iloc[5].plot.bar()
df.iloc[5:8].plot.bar(stacked=True)

df.plot(kind='hist',alpha=0.3, color='b')
df.A.plot(kind='hist',alpha=0.3, color='b')

df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot(kind='barh', stacked=True);
df2['a'].plot.hist(orientation='horizontal', cumulative=True)
df2.plot(kind = 'box')

# Subplots for columns 
df.plot(subplots=True, layout=(2,2))

# Secondary 
ax = df.plot(secondary_y=['A', 'B'])
ax.set_ylabel('CD scale')
ax.right_ax.set_ylabel('AB scale')

# When plt is available
plt.close('all')


# Image processing

import matplotlib.image as mpimg

# The image should be on the current directory (or the folder spyder IDE shows you above see above should contain the image.
# Or you can change path using the following code: import os, os.chdir("your\path\here") ))!!!
img = mpimg.imread('mn.gif')
plt.imshow(img)

# Shape and slice
img.shape
img[1,1]
img[1,216]

# Make writeable
img.flags
img.setflags(write=1)

# Change color
img[1:50,150:200,1:3] = 250



