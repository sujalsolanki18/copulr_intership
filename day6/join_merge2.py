import pandas as pd

# df1 main table
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['sujal', 'vishal', 'bhumi', 'alia']
})

# df2
df2 = pd.DataFrame({
    'ID': [3, 4, 5],
    'Score': [85, 90, 95]
})

inner_merged = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge:\n", inner_merged)

left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:\n", left_join)

right_join = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join:\n", right_join)

# Set index for both DataFrames
df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')

# Join df1 and df2 based on the index
index_join = df1_indexed.join(df2_indexed, how='inner')  

print("\nIndex-Based Join (inner):\n", index_join)



df1_multi = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Dept': ['HR', 'IT', 'HR', 'IT'],
    'Name': ['sujal', 'vishal', 'bhumi', 'alia']
})

df2_multi = pd.DataFrame({
    'ID': [3, 4, 3],
    'Dept': ['HR', 'IT', 'IT'],
    'Score': [85, 90, 75]
})

# Merge on both 'ID' and 'Dept'
multi_key_merge = pd.merge(df1_multi, df2_multi, on=['ID', 'Dept'], how='inner')
print("\nMerge with Multiple Keys:\n", multi_key_merge)
