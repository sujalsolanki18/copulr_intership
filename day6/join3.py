import pandas as pd
df1 = pd.DataFrame({
    'id': [1, 2],
    'name': ['sujal', 'shrey']
})

df2 = pd.DataFrame({
    'id': [3, 4],
    'name':['sourabh', 'vishal']
})

df3 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'score': [85, 90, 95, 80]
})


# Concatenate df1 and df2 (stack them vertically)
df_combined = pd.concat([df1, df2], ignore_index=True)
print("Combined DataFrame (df1 + df2):\n", df_combined)


# Merge the combined DataFrame with df3 on 'id'
merged_df = pd.merge(df_combined, df3, on='id')
print("\nMerged DataFrame:\n", merged_df)
