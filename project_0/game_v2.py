"""Игра угадай число.
Компьютер сам загадывает число, после чего сам угадывает загаданное число"""
import numpy as np


def random_predict(number:int=1) -> int:
    """Функция угадывания

    Args:
        number (int, optional): Загаданное число, по умолчанию 1.

    Returns:
        int: количество попыток
    """

    count = 0 #счетчик количества попыток.
    lower_treshold = 1 #устанавливаем нижнее попроговое значение для генератора.
    upper_treshold = 101 #устанавливаем верхнее попроговое значение для генератора.
    
    while True:        
        count += 1
        predict_number = np.random.randint(lower_treshold, upper_treshold) # предполагаемое число        
        if predict_number > number:
            upper_treshold = predict_number
        elif predict_number < number:
            lower_treshold = predict_number
        else:
            break # выход из цикла, число угадано.
            
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспризводимости
    random_array = np.random.randint(1, 101, size=(1000)) #задали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == '__main__':
    #RUN
    score_game(random_predict)