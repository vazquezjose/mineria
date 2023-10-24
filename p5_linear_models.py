import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataframe = pandas.read_csv("csv/airbnb_study.csv")

dataframe = dataframe[dataframe["num_price"] <= dataframe["num_price"].mean()]
dataframe = dataframe[dataframe["number_of_reviews"] > 5]
dataframe["num_price"] = dataframe["num_price"] / 1000

x = dataframe["review_scores_rating"].values.reshape(-1, 1)
y = dataframe["num_price"].values

model = LinearRegression()

model.fit(x, y)
predicted_y = model.predict(x)

plt.scatter(x, y)
plt.plot(x, predicted_y, color="green")
plt.grid(axis="y")
plt.xlabel("Promedio de las reseñas")
plt.ylabel("Precio por cama en miles de pesos")
plt.title("Relación entre el precio por cama y el promedio de las reseñas") 

plt.savefig("images/p5_linear_models.png")