import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("IT2/Periode_3/aunivers3/pandas/ssbmedier.csv", index_col = 0, skiprows = (0, 1), \
    sep =";", na_values=[".", ".."], encoding = "latin-1")

K = []   # lager ei tom liste K 
startVerdi = 2010   # lager variabel for det første årstallet
for i in range(0, 10):
    K.append(startVerdi + i)
data.columns = K  # setter radoverskriftene i variabelen data lik innholdet av lista K 

print(f"{data}\n")
print(data.describe())

data = data.transpose()
data.plot().legend(bbox_to_anchor = (1, 1))
plt.show()

