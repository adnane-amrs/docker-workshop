import sys
import pandas as pd

print('arguments:', sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({"A": [1, 2], "B": [3, 4], "num_passengers": [5,6], "month": month})
print(df.head())

print(f"Hello Pipeline, month{month}")