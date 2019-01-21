
import matplotlib.pyplot as plt
import numpy as np

#Pyplot tutorial

# Line

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

x = np.linspace(0, 4, 5)

# color, linestyle, linewidth marker
plt.plot(x, x**2, '-.bs', linewidth=3)

plt.plot(x, x**2, color='b', marker='s', markersize = 25, markerfacecolor='w', markeredgecolor='b',linestyle='--', linewidth=2)

# Several
plt.plot(x, x**2, 'ro:', x, x**3, 'bs:')


# Address
plt.ylabel('Some Y numbers')
plt.xlabel('Some X numbers', fontsize=18, color='red')
plt.title('Some title', color = 'b', fontsize=28)

# Axis
plt.axis([0, 6, 0, 70])
plt.ylim(-2, 80)

plt.xticks(fontsize=20, rotation=90)
plt.yticks(np.arange(min(x**3), max(x**3)-10, 10))

# Text
plt.text(3, 30, 'Some text',color='y')
plt.annotate('A point', xy=(4, 64), xytext=(3, 50), color='b',
             arrowprops=dict(facecolor='r', width=2, headwidth = 10, shrink=0.0),
             )

# Grid
plt.grid(False)
plt.grid(which = 'major',axis='x',color='r', linestyle='-.', linewidth=2)

# Setp
lines = plt.plot(x, x**2 )
plt.setp(lines, color='r', linewidth=2.0)
plt.setp(lines, 'color', 'k', 'linewidth', 4.0)
plt.setp(lines, 'marker', 'o')

#plt.show()


# Subplots
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(10, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.title('This is a bar chart')
plt.subplot(132)
plt.scatter(names, values)
plt.title('This is a scatter chart')
plt.subplot(133)
plt.plot(names, values)
plt.title('This is a line chart')
plt.suptitle('Categorical Plotting')
plt.show()

