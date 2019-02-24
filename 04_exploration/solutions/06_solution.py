data.groupby('title').mean()[['rating']].nlargest(10, 'rating')
