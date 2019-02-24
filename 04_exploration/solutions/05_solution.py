(data.groupby(['gender', 'title']).median()[['rating']] >= 4.5).reset_index().groupby('gender').sum()
