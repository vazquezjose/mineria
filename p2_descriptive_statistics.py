import pandas

dataframe = pandas.read_csv("csv/airbnb_study.csv")

columns = [ "accommodates",	"beds", "review_scores_rating", "num_price" ]

for column in columns:
    print(column)
    print(f"\tMedia aritmetica: {dataframe[column].mean()}")
    print(f"\tMediana: {dataframe[column].median()}")
    print(f"\tMinimo: {dataframe[column].min()}")
    print(f"\tMaximo: {dataframe[column].max()}")