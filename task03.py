"""
3. Ввести сроку с клавиатуры, представляющую собой текст.
    3.1. Вывести количество предложений в тексте;
    3.2. Вывести количество слов в тексте;
    3.3. Вывести 3 самых больших слова.
"""
from typing import List


def clear_str(in_str: str) -> str:
    res = ''
    for _ in in_str:
        if _.isalpha():
            res += _.lower()
    return res


def task_3_1(text: str) -> int:
    return len([x for x in text.split()
                if
                x.find('.') >= 0 or
                x.find('!') >= 0 or
                x.find('?') >= 0
                ])


def task_3_2(text: str) -> int:
    counter = 0
    for word in text.split():
        counter += 1 if clear_str(word) != '' else 0
    return counter


def task_3_3(text: str):
    words_weight = {}
    for _ in [clear_str(ss) for ss in text.split()]:
        words_weight[_] = len(_)
    return sorted(words_weight.items(),
                  key=lambda item: -item[1],
                  )[0:3]


if __name__ == "__main__":
    with open("./text_for_03.txt", "rt", encoding="utf-8") as file:
        data = file.read()
    print('Обрабатываемый текст из файла "text_for_03.txt":')
    print('-' * 40)
    print(data)
    print('-' * 40)
    print('Количество предложений в тексте:', task_3_1(data))
    print('Количество слов в тексте:', task_3_2(data))
    print('Три самых длинных слова:', task_3_3(data))

#
# Обрабатываемый текст из файла "text_for_03.txt":
# ----------------------------------------
# Открыли мы файл, а теперь мы хотим прочитать из него информацию...
# Для этого есть несколько способов, но большого интереса заслуживают лишь два из них!
# Первый - метод read, читающий весь файл целиком, если был вызван без аргументов, и n символов,
# если был вызван с аргументом (целым числом n).
# Всем понятен материал?
# ----------------------------------------
# Количество предложений в тексте: 4
# Количество слов в тексте: 50
# Три самых длинных слова: [('заслуживают', 11), ('информацию', 10), ('аргументов', 10)]
#
# Process finished with exit code 0
#
