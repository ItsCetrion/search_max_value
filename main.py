import time
def max_value1(value: list):
    max = None
    for i in value:
        if max == None:
            max = i
        elif max < i:
            max = i
    return max

def max_value2(value: list):
    for i in range(len(value) - 1):
        for j in range(len(value) - i - 1):
            if value[j] > value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]
    return value[-1]
def time_program(value: list, func) -> float:
    "время работы программы с задержкой в 1 секунду"
    start = time.time()
    print(f"максимальное значение в коллекции -> {func(value)}")
    time.sleep(1)
    end = time.time()
    return end - start

def check_mas(value: list) -> bool:
    if isinstance(value[0], (int, float)):
        for i in value:
            if isinstance(i, (int, float)):
                pass
            else:
                return False
        return True
    else:
        for i in value:
            if isinstance(i, type(value[0])):
                pass
            else:
                return False
        return True
def init_list() -> None:
    for i in range(len(collection := input("Введите значения\n").split())):
        if collection[i].replace('.', '', 1).isdigit():
            try:
                collection[i] = int(collection[i])
            except:
                try:
                    collection[i] = float(collection[i])
                except:
                    pass
    return collection
def correct_input(value: list) -> list:
    while not(check_mas(value)):
        print("Поиск максимально значения невозможен, так как имеются разные типы данных\nПовторите ввод данных")
        value = init_list()
    return value

init = correct_input(init_list())
print(f"1-ый алгоритм по поиску максмально значения отработал за {time_program(init, max_value1)}")
print(f"2-ой алгоритм по поиску максмально значения отработал за {time_program(init, max_value2)}")