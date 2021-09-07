import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


def game_core_v3(number):
    '''Устанавливаем число 64 - из логики, что минимальное число ходов будет при целочисленном делении на 2: 101->64->32->16->8->4->2->1.
       Функция принимает загаданное число и возвращает число попыток (через функцию step_logick)'''
    predict = 64
    if number > predict:
        return (step_logick(80, 8, number))  # выход из цикла, если угадали
    elif number < predict:
        return (step_logick(32, 16, number))  # выход из цикла, если угадали
    else:
        return (1)  # выходим с 1й попытки, если number = 64


def step_logick(predict, next_step, number):
    '''Функция принимает начальную позицию и следующий шаг исходя из первоначального диапазона куда попало число number - согласно приложения "Модель ходов + расчет.xlsx".
       И возвращает количество шагов для достижения искомого значения'''
    count = 2  # Входим в функцию уже совершив два хода: [64, 32] или [64, 80].
    while number != predict:
        count += 1
        if number > predict == 88:
            predict = 96
            next_step = 4
        elif number > predict:
            predict += next_step
            next_step = int(next_step / 2)
        else:
            predict -= next_step
            next_step = int(next_step / 2)
    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v1)  # Код с модуля.
score_game(game_core_v2)  # Код с модуля.
score_game(game_core_v3)  # Свой код.
