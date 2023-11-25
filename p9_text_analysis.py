import pandas
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt

dataframe = pandas.read_csv("csv/airbnb_study.csv")

text = ""

a, b = "áéíóúü", "aeiouu"
trans = str.maketrans(a, b)	# table of translation

for string in dataframe["description"].to_list():
	text += str(string).lower().translate(trans)

text = str(re.sub(" +", " ", text))	# extra white space removal

exceptions = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "del", "ya", "que", "se", "es",
"muy", "mediante", "para", "por", "segun", "sin", "so", "sobre", "tras", "versus", "via", "la", "las", "el", "lo", "los", "un", "unos", "y", "u", "e",
"o", "with", "at", "by", "to", "in", "for", "from", "of", "on", "an", "the", "you", "your", "is", "are", "has", "such", "as", "and", "we", "from", "it"]

wc = WordCloud(width=1000, height=1000, background_color="white", stopwords=exceptions)
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")

plt.savefig("images/p9_text_analysis.png")