import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("steam_data.csv")
purchase = df[df["behaviour"]=="purchase"]

game_purchase_value = purchase["game"].value_counts()[0:10].values
game_purchase_index = purchase["game"].value_counts()[0:10].index

color_list = ['peru', 'dodgerblue', 'lightsalmon', 'orange', 'chartreuse', 'red', 'gray', 'skyblue', 'fuchsia', 'olive']

plt.rcParams['figure.dpi'] = 300
fig,ax  = plt.subplots()
ax.barh(game_purchase_index, game_purchase_value, height=0.7,align="center",color=color_list)
ax.set_yticklabels(game_purchase_index)
ax.set_yticks(game_purchase_index)
ax.set_xlabel("Using Amount")
ax.invert_yaxis()
ax.set_title("the most popular games with purchasing")
plt.savefig("purchase_char.jpg")

play = df[df["behaviour"]=="play"]

result = play.groupby("game")["duration"].sum()
sorted_result = result.sort_values(ascending=False)[0:10]
game_play_value = sorted_result.values
game_play_index = sorted_result.index

plt.rcParams['figure.dpi'] = 300
fig,ax  = plt.subplots()
ax.barh(game_play_index, game_play_value, height=0.7,align="center",color=color_list)
ax.set_yticklabels(game_play_index)
ax.set_yticks(game_play_index)
ax.set_xlabel("playing Amount")
ax.invert_yaxis()
ax.set_title("the most popular games with playing")
plt.savefig("play_char.jpg")

sns.set_palette("deep",desat= .6)
sns.set_context(rc={"figure.figsize":(8,5)})

plt.rcParams['figure.dpi'] = 300
play_time = play["duration"]
play_time_index = play_time.index
play_time_value = play_time.values
plt.hist(play_time_value,bins=100,log=True,label="time")
plt.title("Histogram of Play Time")

sns.distplot(play_time_value,bins=100,hist=False,kde=True,kde_kws = {"linewidth" : 2})
plt.title("Density Distribution of Play Time")





