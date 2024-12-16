
import numpy as np # type: ignore
import pandas as pd # type: ignore

df = pd.DataFrame({'Name': ['Ann', 'Bob'], 'Age': [20, 50]})
# print(df)

ds = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print(ds)

# print(df[['Name', 'Age']])
print(df['Name'])
