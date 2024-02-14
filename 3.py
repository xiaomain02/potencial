import csv

#считываем файл
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader=csv.reader(f, delimiter=';')
    rows=list(reader)[1:]
mn=10000000
c=0

n=input() #вводим название категории
while n!='молоко':
    mn=10000000
    c=0
    for i in range(len(rows)):
        if n==rows[i][0]:
            c=1
            if float(rows[i][4])< mn:
                mn=float(rows[i][4])
                p=rows[i][1]
    if c==1: print(f"В категории: {n} товар: {p} был куплен {mn} раз")
    if c==0: print("Такой категории не существует в нашей БД")
    n=input()
