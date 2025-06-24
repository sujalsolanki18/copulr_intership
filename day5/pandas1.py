import pandas as pd

#pandas series from dictionary
dict={'x':19, 'y':26, 'z':36, 'w':40, 'p':58}
s = pd.Series(dict)
print(s)
print()

#pandas series from list
list=[100,200,300,400,500]
s2 = pd.Series(list)
print(s2)
print()


#access the elements of a series in pandas

print("\nindex:",s.iloc[0])
print("\nlable:",s['x'])
print("\nslicing:  ",s[1:3])  