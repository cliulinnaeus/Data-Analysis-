import pandas as pd

df = pd.read_csv('C:/Users/CheLiu/Desktop/20190425165609.csv', delimiter=',')
for stuff in df:
    print(stuff)
