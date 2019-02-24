mask_title = (data.groupby('title').count()['rating'] >= 100).reset_index()
df = data.merge(mask_title, how='inner', left_on='title', right_on='title')

data_popular = df[df['rating_y']]
mean_ratings = data_popular.pivot_table(values='rating_x', index='title',
                                        columns='gender', aggfunc='mean')

mean_ratings.sort_values(by='F', ascending=False).head(10) #top 10 féminin

mean_ratings.sort_values(by='M', ascending=False).head(10) #top 10 masculin

mean_ratings.plot(x='F', y='M', kind='scatter', figsize=(5,5))
