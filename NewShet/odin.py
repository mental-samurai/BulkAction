#csv -comma separated values +
import csv

# with open('sq.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=';',
#                         quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     for i in range(10):
#         writer.writerow([i, i ** 2, f'{i} = {i ** 2}'])

goods = [('Табурет', 1000),('Диван', 1001), ('Стул', 1002),
         ('Скамья', 1003),('Люстра', 1004)]

with open('../../../Desktop/sq.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    for i in goods:
        writer.writerow(i)
        print(i)
data = [{
    'lastname': 'Кузнецов',
    'firstname': 'Петр',
    'сlass': '9',
    'class_letter': 'A'
}, {
    'lastname': 'Меньшов',
    'firstname': 'Алексей',
    'сlass': '9',
    'class_letter': 'A'
    }]
with open('../form.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
                            delimiter=':', quoting=csv.QUOTE_NONNUMERIC)

    writer.writeheader()
    for item in data:
        writer.writerow(item)

with open('../form.csv', 'w', newline='') as f:
    reader = csv.DictReader(f, delimiter=':', quoting=csv.QUOTE_NONNUMERIC)
    for item in reader:
        for k, v in item.items():
            print(k, v)
