import pandas as pd
import numpy as np

df = pd.read_csv("steam_data.csv")

play = df[df["behaviour"]=="play"]
play = play[0:1000]

play["rating"] = 0;

play.describe()
for i in np.arange(0,1,0.2):
    print (play.quantile(i))

rating = []
for duration in play["duration"]:
    if duration < 0.7:
        rating.append(1)
    elif duration < 2.6:
        rating.append(2)
    elif duration < 7.0:
        rating.append(3)
    elif duration < 1.962000e+01:
        rating.append(4)
    else:
        rating.append(5)
play["rating"] = rating

play.to_csv("sample_data.csv",index=False)




