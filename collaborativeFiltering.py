import pandas as pd
import numpy as np
import matrix_factorization_utilities


df = pd.read_csv("sample_data.csv")
df1 = df[["userId", "game", "rating"]]
rating_df = pd.pivot_table(df1,
                           index ="userId",
                           columns = "game")

rating_df.to_csv("rating_matix.csv",index = False)
U,V = matrix_factorization_utilities.low_rank_matrix_factorization(rating_df.as_matrix(),
                                                                 num_features=15,
                                                                 regularization_amount=0.1)
predicted_ratings = np.matmul(U,V)

predicted_ratings_df = pd.DataFrame(index = rating_df.index,
                                    columns = rating_df.columns,
                                    data= predicted_ratings)

predicted_ratings_df.to_csv("predicted_rating.csv",index = False)

nrows, ncols = predicted_ratings.shape
users = df["userId"].unique().tolist()
games = df["game"].unique().tolist()
table = { }
for i in range(len(df)):
    (user, game) = (df["userId"].iloc[i], df["game"].iloc[i])
    table[(user, game)] = df["rating"].iloc[i]
    
for row in range(nrows):
    for col in range(ncols):
        (user, game) = (users[row], games[col])
        if (user, game) in table:
            predicted_ratings[row, col] = np.nan

max_game = [ ]
for row in range(nrows):
    gameIndex = np.argmax(predicted_ratings[row, :])
    max_game.append(games[gameIndex])
    