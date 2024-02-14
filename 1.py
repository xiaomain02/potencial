import csv

#считываем файл
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader=csv.reader(f, delimiter=';')
    rows=list(reader)[1:]

k=0  #итоговая сумма по категории "Закуски"

#добавляем в список значения выручки по продуктам
for i in range(len(rows)):
    rows[i].append(str(float(rows[i][3])*float(rows[i][4])))
    if rows[i][0]=="Закуски": k+=float(rows[i][5])
print(k)

#создаём новый файл
with open('products_new.csv', 'w', encoding='utf-8-sig', newline="") as f1:
    writer=csv.writer(f1, delimiter=';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    writer.writerows(rows)
