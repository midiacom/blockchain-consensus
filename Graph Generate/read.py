import pandas as pd

df = pd.read_csv("soc-sign-bitcoinotc.csv")

print(df.head())

source = df["6"]

target = df["2"]

rating = df["4"]

timestamp = df["1289241911.72836"]

dict_st_tmp = {}

for i in range(len(source)):
    dict_st_tmp[(source[i],target[i])] = []

print(dict_st_tmp)
