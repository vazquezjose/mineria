import pandas

dataframe = pandas.read_csv("csv/airbnb.csv")

useless_columns = [ "listing_url", "scrape_id", "last_scraped", "source", "picture_url",
    "host_url", "host_location", "host_response_time", "host_response_rate", "host_acceptance_rate",
    "host_is_superhost", "host_thumbnail_url", "host_picture_url", "host_neighbourhood",
    "host_verifications", "host_has_profile_pic", "host_identity_verified", "neighbourhood",
    "neighbourhood_group_cleansed", "latitude", "longitude", "bathrooms", "bathrooms_text",
    "bedrooms", "calendar_updated", "has_availability", "availability_30", "availability_60",
    "availability_90", "availability_365", "calendar_last_scraped", "number_of_reviews_ltm",
    "first_review", "last_review", "review_scores_accuracy", "review_scores_cleanliness",
    "review_scores_checkin", "review_scores_communication", "review_scores_location",
    "review_scores_value", "license", "instant_bookable" ]

# eliminar columnas inutiles
dataframe = dataframe.drop(useless_columns, axis=1)

useless_desc_keys = [ "The space", "Guest access", "<br />", "<b>", "<br/>", "</b>", "<br /", "<br/", "<br", "<b" ]

# eliminar frases inutiles y tags de html
for key in useless_desc_keys:
    dataframe["description"] = dataframe["description"].str.replace(key, "")
    dataframe["neighborhood_overview"] = dataframe["neighborhood_overview"].str.replace(key, "")

# agregar columna de precio solo numerico
dataframe["num_price"] = dataframe["price"].str.replace("$", "")
dataframe["num_price"] = dataframe["num_price"].str.replace(",", "")
dataframe["num_price"] = dataframe["num_price"].str.replace(".00", ".0")
dataframe["num_price"] = pandas.to_numeric(dataframe["num_price"])

# agregar columna de precio por cama
dataframe["price_per_bed"] = dataframe["num_price"] / dataframe["beds"]

# eliminar caracteres especiales de las columnas con texto
dataframe["description"] = dataframe["description"].str.replace(r'[^A-zÀ-ú]+', " ", regex=True)
dataframe["neighborhood_overview"] = dataframe["neighborhood_overview"].str.replace(r'[^A-zÀ-ú ]+', " ", regex=True)
dataframe["host_about"] = dataframe["host_about"].str.replace(r'[^A-zÀ-ú ]+', " ", regex=True)

# eliminar filas de la columna "beds" con datos vacios
dataframe.dropna(subset=["beds"], inplace=True)

# llenar las filas con reviews vacias con 0
dataframe["review_scores_rating"].fillna(0.0, inplace=True)
dataframe["reviews_per_month"].fillna(0.0, inplace=True)

# exportar csv con formato
dataframe.to_csv("csv/airbnb_study.csv", index=False)