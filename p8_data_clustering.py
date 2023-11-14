import matplotlib.pyplot as plt
import pandas
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans

def get_cmap(n, name="hsv"):
	"""Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
	RGB color; the keyword argument name must be a standard mpl colormap name."""
	return plt.cm.get_cmap(name, n)

dataframe = pandas.read_csv("csv/airbnb_study.csv")

dataframe = dataframe[dataframe["num_price"] <= dataframe["num_price"].mean()]
dataframe = dataframe[dataframe["number_of_reviews"] > 5]
dataframe["num_price"] = dataframe["num_price"] / 1000

dataframe.rename(columns={"neighbourhood_cleansed": "Alcaldía"}, inplace=True)

############################################

fig, ax = plt.subplots()
labels = pandas.unique(dataframe["Alcaldía"])
cmap = get_cmap(len(labels) + 1)
l = list()
for i, label in enumerate(labels):
	filter_df = dataframe.query(f"Alcaldía == '{label}'")
	l.append(ax.scatter(filter_df["review_scores_rating"], filter_df["num_price"], label=label, color=cmap(i)))

plt.legend(handles=l)
plt.xlabel("Promedio de las reseñas")
plt.ylabel("Precio por cama en miles de pesos")
plt.tight_layout()
plt.savefig("images/p8_forecasting_1.png")
plt.close()

############################################

X = dataframe[["review_scores_rating", "num_price"]]
Y = dataframe["Alcaldía"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

X_train_norm = normalize(X_train)
X_test_norm = normalize(X_test)

kmeans = KMeans(n_clusters = 16, random_state = 0, n_init = "auto")
kmeans.fit(X_train_norm)

sns.scatterplot(data = X_train, x = "review_scores_rating", y = "num_price", hue = kmeans.labels_)
plt.xlabel("Promedio de las reseñas")
plt.ylabel("Precio por cama en miles de pesos")
plt.tight_layout()
plt.savefig("images/p8_forecasting_2.png")