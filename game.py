

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 500)
        if number == predict_number:
            break # выход из цикла
    return(count)
    
    


def score_game(random_predict) -> int:
    """Проверяем эффективность алгоритма на 1000 числах
    
    Args:
        random_predict (функция): _description_

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #список 1000 чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
    
print('here the commit mark1')

    #print(f'количество попыток: {random_predict(10)}')