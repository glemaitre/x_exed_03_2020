data_popular = data
mean_ratings = data_popular.pivot_table(values='rating', index='title',
                                        columns='gender', aggfunc='mean')

mean_ratings.sort_values(by='F', ascending=False).head(10) #top 10 féminin
mean_ratings.sort_values(by='M', ascending=False).head(10) #top 10 masculin

mean_ratings.plot(x='F', y='M', kind='scatter', figsize=(5,5))
