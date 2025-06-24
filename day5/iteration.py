import pandas as pd

#diffrent way to iterate over rows in pandas dataframe
df = pd.DataFrame({
    'Name': ['sujal', 'vishal', 'rudra'],
    'Age': [25, 30, 28],
    'City': ['jaipur', 'delhi', 'mumbai']
})

for i ,row in df.iterrows():
    print(row['Name'], row['Age'])
print()
    
# Selecting rows based on a condition
print(df[df['Age'] > 25])
print()

# select any row using iloc[]
print(df.iloc[1]) 
print(df['Name'][:3])
print()

#drop rows based on condition
df1=df[df['Age'] > 25]
print(df1)
print()

# insert row at given position 
r=pd.DataFrame([['pawan', 20, 'delhi']], columns=['Name', 'Age', 'City'])
df2=pd.concat([df, r], ignore_index=True)
print(df2)
print()

# list from rows
r_list=df.to_dict('records')
print(r_list)
