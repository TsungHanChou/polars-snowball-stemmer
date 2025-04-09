import polars as pl
from polars_snowball_stemmer import snowball_stem

df = pl.DataFrame({
    'word': [
        "hopelessly", 
        "fearfulness", 
        "amazingly", 
        "careless", 
        "beautifully", 
        "kindness"
    ]
})

print(df.with_columns(b=snowball_stem('word')))
