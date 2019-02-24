data.groupby('movie_id')['rating'].mean().hist(bins=20)
