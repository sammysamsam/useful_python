import pandas as pd


### 
# pandas
###


df = pandas.DataFrame()

# print column types
non_numerics = [type(df[x][0]) for x in df.columns]
