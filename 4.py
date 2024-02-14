import csv

def promo(a, b):
    '''
    Функция генерирует промокоды для продуктов
    :param a: строка, название продукта
    :param b: строка, дата поступления продукта
    :return: функция возвращает сгенерированный код в формате строки
    '''
    s=''
    s=s+a[:2].upper()+b[:2]+a[-1].upper()+a[-2].upper()+b[4]+b[3]
    return s

#считываем файл
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader=csv.reader(f, delimiter=';')
    rows=list(reader)[1:]

#добавляем сгенерированный промокод в список
for i in range(len(rows)):
    rows[i].append(promo(rows[i][1], rows[i][2]))

print(rows)
#создаём новый файл
with open('product_promo.csv', 'w', encoding='utf-8-sig', newline="") as f1:
    writer=csv.writer(f1, delimiter=';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promo'])
    writer.writerows(rows)
