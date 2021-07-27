import pandas as pd
rawdata = pd.read_csv("D:/Amarthiga/PracticingCodes/Data/netflix_titles.csv")
print(rawdata)

dataframe = pd.DataFrame(rawdata)

print(dataframe.shape)
