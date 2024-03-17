import pandas as pd

a_dick = {'ksi':1, 'david':2, 'linux':3}
series = pd.Series(a_dick)

rangeAcces0 = series[0:1]

rangeAcces1 = series[1]

rangeAcces2 = series['ksi']

data = {
    'calories':[123,444,340],
    'duration':[40,20,30]
}
df = pd.DataFrame(data)
print(df)

