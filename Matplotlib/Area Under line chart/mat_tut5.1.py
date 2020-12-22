from matplotlib import pyplot as plt
import csv
import pandas as pd
plt.style.use("seaborn-dark")
"""
This is simple line chart but with area underneath
Note::: Alpha helps us to control the opacity
"""

# with open("mat_tut5.1.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     py_dev_y = []
#     dev_y = []
#     ages_x = []
#     for row in csv_reader:
#         py_dev_y.append(row["Python"])
#         dev_y.append(row["All_Devs"])
#         ages_x.append(row["Age"])
#

data = pd.read_csv("mat_tut5.1.csv")
ages_x = data["Age"]
dev_y = data["All_Devs"]
py_dev_y = data["Python"]

plt.plot(ages_x, py_dev_y, label= "Python Developer", linestyle = "--")

plt.plot(ages_x, dev_y, label= "All Developer", linestyle = "-")

av_median = 57287
plt.fill_between(ages_x,py_dev_y,dev_y,
                 where=(py_dev_y > dev_y), color="red",interpolate=True, alpha=0.25, label="Above Avg")
#
plt.fill_between(ages_x,py_dev_y,dev_y,
                   where=(py_dev_y < dev_y),color="blue",interpolate=True, alpha=0.25, label="Below Avg")

plt.legend()
plt.title("Area Under Line Chart")
plt.xlabel("Ages")
plt.ylabel("Median Salary")
plt.tight_layout()
plt.savefig("Area under line chart.png")
plt.show()




