import csv

#считываем файл
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader=csv.reader(f, delimiter=';')
    rows=list(reader)[1:]

a=[]
#добавляем в список значения выручки по продуктам
for i in range(len(rows)):
    b=[]
    b.append(rows[i][1])
    b.append(rows[i][0])
    b.append(rows[i][4])
    a.append(b)

#сортируем список в алфавитном порядке по продаже 
for i in range(1, len(a)):
    x=a[i]
    j=i
    while j>0 and float(a[j-1][2])>float(x[2]):
        a[j]=a[j-1]
        j-=1
    a[j]=x

#выводим 10 наименее продаваемых продуктов
for i in range(10):
    print(a[i][1], a[i][2])

