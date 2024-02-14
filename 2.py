import csv

#считываем файл
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader=csv.reader(f, delimiter=';')
    rows=list(reader)[1:]

mx=0  #цена самого дорогого товара
ct='' #название продукта самого дорогого товара

#сортируем список в алфавитном порядке по категориям 
for i in range(1, len(rows)):
    x=rows[i]
    j=i
    while j>0 and rows[j-1][0]>x[0]:
        rows[j]=rows[j-1]
        j-=1
    rows[j]=x

for i in range(len(rows)):
    if rows[i][0]==rows[0][0]:
        if mx<float(rows[i][3]):
            mx=float(rows[i][3])
            ct=rows[i][1]
print(f'В категории: {rows[0][0]} самый дорогой товар: {ct} его цена за единицу товара составляет {mx}')
