import polars as pl
import polars_snowball_stemmer as stemmer

df = pl.DataFrame({'word': ["fearlessly", "littleness", "lovingly", "devoted"]})
print(df.with_columns(b=stemmer.snowball_stem('word')))