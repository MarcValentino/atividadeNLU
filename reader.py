import pandas as pd

csv = pd.read_csv("cartas_van_gogh.csv", low_memory=False, keep_default_na=False)

print(csv.head(10))