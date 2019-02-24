mask_title = (data.groupby('title').count()['rating'] >= 30).reset_index()
df = data.merge(mask_title, how='inner', left_on='title', right_on='title')

df[df['rating_y']].groupby('title').mean()['rating_x'].plot(kind='kde')
df[~df['rating_y']].groupby('title').mean()['rating_x'].plot(kind='kde')
