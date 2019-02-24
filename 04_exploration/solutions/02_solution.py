for group, df in data.groupby('gender'):
    counts = (data['rating'] >= 4.5).value_counts()
    print(f'{group} => {counts}\n')
