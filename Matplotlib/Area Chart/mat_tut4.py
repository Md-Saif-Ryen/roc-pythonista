from matplotlib import pyplot as plt
plt.style.use("ggplot")

"""
This is a Stack Plot.
Its kinda plotted pie chart.
That is like A pie chart plotted at different range of sequence or interval of time.
Here,We don't measure it like in simple plotting mean from the origin,
We just measure the area covered at certain point of time,That's why I call it plotted Pie Chart as it is like 
plotting the pie chart at certain time interval or a sequence.

--------------------It is used when comparing different objects at a uniform sequence------------
"""
minutes = [1,2,3,4,5,6,7,8,9]
player1 = [1,2,0,3,2,1,4,5,3]
player2 = [1,3,2,5,1,3,5,3,2]
player3 = [2,3,5,1,3,0,3,0,3]
labels = ["Player1", "Player2", "Player3"]

plt.stackplot(minutes, player1,player2,player3, labels=labels)

plt.legend()
plt.xlabel("Time(min)")
plt.ylabel("Scores")
plt.title("My Awesome Plotted Pie Chart")
plt.savefig("Stack Plot.png")
plt.tight_layout()
plt.show()