import pandas as pd
import numpy as np

df = pd.read_csv("steam_data.csv")

purchase = df[df["behaviour"]=="purchase"]
play = df[df["behaviour"]=="play"]

sorted_time= play.sort_values(by="duration")
sorted_time["rating"] = 0

sorted_time.describe()

for i in np.arange(0,1,0.2):
    print (sorted_time.quantile(i))

rating = []
for duration in sorted_time["duration"]:
    if duration < 0.7:
        rating.append(1)
    elif duration < 2.8:
        rating.append(2)
    elif duration < 7.9:
        rating.append(3)
    elif duration < 28:
        rating.append(4)
    else:
        rating.append(5)
sorted_time["rating"] = rating

sorted_time.to_csv("game_play_rating.csv", index = False)


   