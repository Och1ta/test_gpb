import os
import time


sec_on_day = 86_400  # 86400 секунд в дне


def remove_old_files(folder_path, days):
    # Получаем текущее время
    now = time.time()

    # Вычисляем время, которое было N дней назад
    cutoff = now - (days * sec_on_day)

    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Проверяем, является ли путь файлом
        if os.path.isfile(file_path):
            # Получаем время последнего изменения файла
            file_mtime = os.path.getmtime(file_path)

            # Если файл старше N дней, удаляем его
            if file_mtime < cutoff:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")


# Пример использования
folder_path = "/path/to/your/folder"  # Укажите путь к вашей папке
days = 30  # Укажите количество дней
remove_old_files(folder_path, days)
