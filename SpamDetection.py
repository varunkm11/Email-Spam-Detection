import pandas as pd

data = pd.read_csv("D:\CV Projects\Email-Spam-Detection\spam.csv")
print(data.shape)
data.drop_duplicate(inplace=True)