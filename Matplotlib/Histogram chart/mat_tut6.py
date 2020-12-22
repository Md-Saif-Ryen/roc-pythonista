import matplotlib.pyplot as plt
import pandas as pd

"""
Histogram is used to plot data in which we visualize the frequency of an object in a range(bin).
A list of objects and frequency of objects in certain ranges.
"""
plt.style.use("seaborn-dark")

data = pd.read_csv("mat_tut6.csv")

ids = data["Responder_id"]
ages = data["Age"]

bin = [10,20,30,40,50,60,70,80,90,100]

plt.hist(ages, bins=bin, log=True, edgecolor="w",color="k")
median_age = 29
plt.axvline(median_age, color="grey", label="Median Age")
plt.legend()

plt.title("Responding Ages")
plt.xlabel("Ages")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Histogram.png")
plt.show()
