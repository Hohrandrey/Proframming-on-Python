#1 вариант решения
def main(table_data):
    unique_data = []
    seen_rows = set()

    for row in table_data:
        if tuple(row) not in seen_rows:
            unique_data.append(row)
            seen_rows.add(tuple(row))

    transformed_data = []
    for row in unique_data:
        value = float(row[0].strip('%')) / 100
        new_row = [f"{value:.3f}"]

        phone_number = ''.join(filter(str.isdigit, row[1]))[3:]
        new_row.append(phone_number)

        name_parts = row[2].split(' ')
        full_name = (
            f"{name_parts[0]} {name_parts[-1]}"
            if len(name_parts) >= 2
            else row[2]
        )
        new_row.append(full_name.replace('.', ''))

        answer_map = {'Да': 'Y', 'Нет': 'N'}
        new_row.append(answer_map.get(row[3], row[3]))

        transformed_data.append(new_row)

    return transformed_data


# Пример запуска с предопределёнными данными
table_data = [
    ['1%', '839-184-8847', 'Артур Ш. Шунук', 'Нет'],
    ['11%', '726-737-0807', 'Константин Ф. Виришич', 'Да'],
    ['3%', '206-317-0211', 'Платон Ч. Чичечко', 'Нет'],
    ['4%', '208-416-5030', 'Борис О. Вузолко', 'Нет'],
    ['4%', '208-416-5030', 'Борис О. Вузолко', 'Нет'],  # Повторяющаяся строка
]

transformed_table = main(table_data)
for row in transformed_table:
    print("\t".join(row))

#2 вариант решения
