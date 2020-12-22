from matplotlib import pyplot as plt
import numpy as np
plt.style.use("seaborn-dark")

"""
This is quite same as line chart but instead of using line to compare,It uses bars to compare.
This method of data visualization should be used when comparing more than 5 objects.
"""

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# This is basically indexing all the ages to to a range equal to its length
# This is to avoid coinciding of all the bars
# we subtract with a width in order to slightly move the bar a bit back or a bit forward
array = np.arange(len(ages_x))


width = 0.25
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287]

plt.bar(array - width, py_dev_y,width=width, label='Python')

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293]

plt.bar(array, js_dev_y, width=width,label='JavaScript')

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320]

plt.bar(array + width, dev_y,width=width , label='All Devs')


plt.legend()
plt.xticks(array, ages_x)

plt.title('Median Salary (IND) by Age')

plt.xlabel('Ages')
plt.ylabel('Median Salary (IND)')




plt.tight_layout()



plt.savefig('plot.png')


plt.show()
