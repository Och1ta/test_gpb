m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

# 1. Общее количество чисел
total_count = sum(len(s) for s in m)
print(f"Общее количество чисел: {total_count}")

# 2. Общая сумма чисел
total_sum = sum(sum(s) for s in m)
print(f"Общая сумма чисел: {total_sum}")

# 3. Среднее значение
average = sum(sum(s) for s in m) / sum(len(s) for s in m)
print(f"Среднее значение: {average}")

# 4. Собрать все множества в один кортеж
combined_tuple = tuple(set().union(*m))
print(f"Все множества в одном кортеже: {combined_tuple}")
