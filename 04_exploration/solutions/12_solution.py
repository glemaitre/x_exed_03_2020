df = data.groupby(['gender', 'title']).mean()[['rating']].reset_index()
fig, ax = plt.subplots()
for group, sub_df in df.groupby('gender'):
    sub_df.hist(ax=ax, alpha=0.3, label=group)
plt.legend()
