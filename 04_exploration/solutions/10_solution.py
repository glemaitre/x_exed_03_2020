data.groupby('movie_id')['rating'].count().hist(bins=10)
