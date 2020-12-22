import pandas as pd
import matplotlib.pyplot as plt


"""
THis is my scatter plotting which is very useful when comparing two sets of objects or elements 
In this case those two sets or elements are like/view plotting and ratio/color relation.
"""
plt.style.use("seaborn-dark")

data = pd.read_csv("mat_tut7.2.csv")
views = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(views,likes,c=ratio, cmap="summer",edgecolors="black", linewidths=1,alpha=0.75)

plt.colorbar().set_label("Like/Dislike ratio")
plt.xscale("log")
plt.yscale("log")



plt.title("Trending Videos on YT")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.tight_layout()
plt.savefig("Trending videos.png")
plt.show()