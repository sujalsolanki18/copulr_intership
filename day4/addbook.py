import csv
address_book =[['name','address','mobile','email'],['sujal','jaipur','9876545665','gdhs@gmail.com'],['vishal','kota','9473824532','fhdj@gmail.com'],
               ['sourabh','bundi','9384483234','bcgdsh@gmail.com']]
with open('address_book.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    for x in address_book:
        writer.writerow(x)
