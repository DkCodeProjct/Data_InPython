import pandas as pd




df =  pd.read_csv(input('csv: ')) # pd.read_csv('ItemData0.csv')

choice = int(input('1. Print data to String:\n2. Print Headers: '))

if choice == 1:
    print(df.to_string())
else:
    print(df.head())

