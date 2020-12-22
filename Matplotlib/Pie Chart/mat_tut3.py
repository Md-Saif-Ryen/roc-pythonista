from matplotlib import pyplot as plt


"""
This is a pie chart.
We should use it when comparing 5 or less than 5 objects in general for clarity.
"""

plt.style.use("seaborn")

slices = [20046, 17100, 20000, 24744, 30500]

labels = ["Python", "Java", "PHP", "Ruby", "Swift"]
explode = [0.1, 0.09, 0.01, 0.0921, 0.032]

plt.pie(slices, labels=labels, wedgeprops={"edgecolor": "black"}, autopct="%1.1f%%", shadow=True,explode=explode,startangle=90)



plt.title("My Awesome Pie Chart")
plt.savefig("Pia Chart.png")

plt.show()