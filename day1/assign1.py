a=input("enter your name:")
b=input("enter your class")
c=int(input("enter 1st subject marks:"))
d=int(input("enter 2nd subject marks:"))
e=int(input("enter 3rd subject marks:"))
f=int(input("enter 4th subject marks:"))
g=int(input("enter 5th subject marks:"))

total_marks = c+d+e+f+g
percentage = total_marks/5

print("result of",a,"of class",b,"is",percentage )



a="hello"
b="python"
c=a+b
print(c)
print(c.upper())
print(c.lower())
print("Uppercase:", c.upper())
print("Lowercase:", c.lower())
print("Title Case:",c.title())
print("Length of string:", len(c))
print("Reverse String:", c[::-1])