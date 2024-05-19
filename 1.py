import csv
from collections import defaultdict

# Путь к файлу CSV
file_path = '1_test.csv'

# Чтение данных из файла
records = []
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        records.append(row)

# Словарь для хранения уникальных записей и для проверки дублирующихся ID
unique_records = {}
duplicate_records = defaultdict(list)

# Обработка записей
for record in records:
    record_id = record['id'].strip()
    if record_id in unique_records:
        if unique_records[record_id] != record:
            duplicate_records[record_id].append(record)
            if unique_records[record_id] not in duplicate_records[record_id]:
                duplicate_records[record_id].append(unique_records[record_id])
    else:
        unique_records[record_id] = record

# Конвертация уникальных записей в список для дальнейшего использования
unique_records_list = list(unique_records.values())

# Вывод результатов
print("Уникальные записи:")
for record in unique_records_list:
    print(record)

print("\nЗаписи с дублирующимися ID:")
for record_id, records in duplicate_records.items():
    print(f"ID: {record_id}")
    for record in records:
        print(record)
