mask_men = data['gender'] == 'F'
mask_age = data['age'] > 30
(data[mask_men & mask_age].groupby('title').median()['rating'] >= 4.5).value_counts()
