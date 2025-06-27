import time
import sys


# Пример с использованием итератора (список)
def create_list(n):
    return [i for i in range(n)]


# Пример с использованием генератора
def create_generator(n):
    return (i for i in range(n))


# Функция для измерения времени выполнения
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return end_time - start_time, result


# Функция для измерения потребления памяти
def measure_memory(result):
    size_in_bytes = sys.getsizeof(result)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024
    size_in_gb = size_in_mb / 1024
    return size_in_bytes, size_in_kb, size_in_mb, size_in_gb


# Функция для форматирования размера памяти
def format_memory_size(size_in_bytes, size_in_kb, size_in_mb, size_in_gb):
    return f"{size_in_bytes} байт, {size_in_kb:.2f} КБ, {size_in_mb:.2f} МБ, {size_in_gb:.2f} ГБ"


# Параметры для тестирования
n = 10**8   # Большое число для демонстрации разницы

# Измерение времени и памяти для итератора (списка)
list_time, list_result = measure_time(create_list, n)
list_memory = measure_memory(list_result)

# Измерение времени и памяти для генератора
gen_time, gen_result = measure_time(create_generator, n)
gen_memory = measure_memory(gen_result)

# Вывод результатов
print(f"Время выполнения для списка: {list_time:.6f} секунд")
print(f"Потребление памяти для списка: {format_memory_size(*list_memory)}")
print(f"Время выполнения для генератора: {gen_time:.6f} секунд")
print(f"Потребление памяти для генератора: {format_memory_size(*gen_memory)}")
