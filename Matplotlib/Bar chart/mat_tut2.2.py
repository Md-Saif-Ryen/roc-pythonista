from matplotlib import pyplot as plt
import csv
from collections import Counter
# import pandas as pd

"""
Here We are importing data as a Csv file to visualize.
We should use horizontal bar when comparing many objects. 
NOte------------Pandas open csv as column wise dictionary
and csv open csv as row wise dictionary
"""


"""
Using Csv
"""
plt.style.use("seaborn-dark")
with open("text.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)  #reading the csv file as a Dictionary

    language_counter = Counter()  #To know the frequency of a language here

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))   #We are passing a string as a list in counter to know the friquency of languages here



"""
Using Pandas
"""
# data = pd.read_csv("text.csv")
# ids = data["Responder_id"]
# lang_responses = data["LanguagesWorkedWith"]
# language_counter = Counter()
#
# for responses in lang_responses:
#     language_counter.update(responses.split(";"))



languages =[]
popularity = []
for i in language_counter.most_common(15):
    languages.append(i[0])
    popularity.append(i[1])


languages.reverse()
popularity.reverse()
plt.barh(languages, popularity, color="k")

plt.title("Programming Languages Popularity")
plt.xlabel("Number of People Using")
plt.ylabel("Programming Language")

plt.tight_layout()
plt.savefig("Popular Languages.png")
plt.show()





