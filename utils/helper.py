import pandas as pd

def split_genres(df):

    genres = []

    for item in df["listed_in"]:
        genres.extend(item.split(","))

    return pd.Series(genres).str.strip()