mask_title = data.groupby('title').count()['rating'] > 30
data.groupby('title').median()[mask_title][['rating']].nlargest(10, 'rating')
