import pandas as pd  

data = pd.read_csv("Global YouTube Statistics.csv", index_col = 0, skiprows = (0), \
                   sep = ",", na_values = [".", ".."], encoding = "latin-1")

print(data)