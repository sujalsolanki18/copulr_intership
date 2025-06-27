import pandas as pd

df=pd.DataFrame({
    'email':['sujal4040@gmail.com', 'shrey2394@gmail.com'],
    'mobile':['9876543210', '95885858@34'],
    'city':['Delhi', 'Mumbai234'],
    'price':['$40*','$50 dollar added'],
    'pasword':['s'
    'kumar@123', 'hello4@sjf123']
    
})
df['mobile'] = df['mobile'].str.replace(r'\D','', regex=True)
df['city'] = df['city'].str.replace(r'[^a-zA-Z]','', regex=True)
df['price'] = df['price'].str.replace(r'\D','', regex=True).astype(int)
df['pasword'] = df['pasword'].str.replace(r'\W','', regex=True)
df['email'] = df['email'].str.replace(r'@.*','', regex=True)

    
print(df)