import pandas
import scipy.stats as stats

dataframe = pandas.read_csv("csv/airbnb_study.csv")

resultado = stats.f_oneway(dataframe["review_scores_rating"].tolist(), dataframe["num_price"].tolist())

print("Estadístico F:", resultado.statistic)
print("P-valor:", resultado.pvalue)