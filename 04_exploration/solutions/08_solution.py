(data.groupby('title').aggregate(['mean', 'count'])[['rating']]
                      .sort_values(by=[('rating', 'count')], ascending=False)
                      .head(1))
