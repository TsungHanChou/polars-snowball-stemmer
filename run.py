import polars as pl
from polars_snowball_stemmer import snowball_stem

df = pl.DataFrame({'word': ["fearlessly", "littleness", "lovingly", "devoted"]})
print(df.with_columns(b=mp.snowball_stem('word')))