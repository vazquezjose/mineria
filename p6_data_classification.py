import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

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
plt.savefig("images/p6_data_classification_real.png")
plt.close()

############################################

X = dataframe[["review_scores_rating", "num_price"]]
y = dataframe["Alcaldía"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with k = 3:", accuracy)

############################################
'''
k_values = [i for i in range(1, 100)]
scores = []

scaler = StandardScaler()
X = scaler.fit_transform(X)

for k in k_values:
	knn = KNeighborsClassifier(n_neighbors=k)
	score = cross_val_score(knn, X, y, cv=5)
	scores.append(np.mean(score))

ax = sns.lineplot(x = k_values, y = scores, marker = 'o')
plt.xlabel("K Values")
plt.ylabel("Accuracy Score")
plt.savefig("images/p6_data_classification_k_values.png")
'''
############################################

X = dataframe[["review_scores_rating", "num_price"]]
y = dataframe["Alcaldía"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=60)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with k = 60:", accuracy)