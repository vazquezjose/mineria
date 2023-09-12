import pandas
import matplotlib.pyplot as plt

dataframe = pandas.read_csv("csv/airbnb_study.csv")
fig, ax = plt.subplots()

amount_of_landlords = 10

x = dataframe[["host_id", "host_name"]].value_counts().head(amount_of_landlords)

property_landlord_names = list(map(lambda a: a[1], x.keys()))
property_amounts = x.to_list()

ax.bar(property_landlord_names, property_amounts, align="center")

plt.xlabel("Alias del casero")
plt.ylabel("Número de propiedades")
plt.title("Caseros en la CDMX con mayor numero de\npropiedades anunciadas en AirBNB")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("images/p3_data_visualization.png")