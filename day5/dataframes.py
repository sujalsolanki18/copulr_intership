import pandas as pd

#dataframe with a two dimensional list
list=[[1,'sujal'],[2,'sourabh'],[3,'vishal'],[4,'pratik'],[5,'suraj']]
df = pd.DataFrame(list, columns=['id', 'name'])
print(df)


#dataframe with a dictionary
dict={'name':['sujal','sourabh','vishal','pratik','suraj'],'age':[20,21,22,23,24],'city':['delhi','mumbai','pune','bangalore','hyderabad']}
df2 = pd.DataFrame(dict)
print("\n", df2)

#using list if lists
list=[['sujal',20,'delhi'],['sourabh',21,'mumbai'],['vishal',22,'pune'],['pratik',23,'bangalore'],['suraj',24,'hyderabad']]
df3 = pd.DataFrame(list, columns=['name', 'age', 'city'])
print("\n", df3)

# using list of tuples
list=[('sujal',20,'delhi'),('sourabh',21,'mumbai'),('visha',22,'pune'),('pratik',23,'bangalore'),('suraj',24,'hyderabad')]

df4 = pd.DataFrame(list)
print("\n", df4)


# using list of dictionaries
list=[{'name':'sujal','age':20,'city':'delhi'},{'name':'sourabh','age':21,'city':'mumbai'},{'name':'vishal','age':22,'city':'pune'},{'name':'pratik','age':23,'city':'bangalore'},{'name':'suraj','age':24,'city':'hyderabad'}]

df5 = pd.DataFrame(list)
print("\n", df5)