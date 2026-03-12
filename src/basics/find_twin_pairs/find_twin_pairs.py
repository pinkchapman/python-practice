import math

def find_twin_pairs(X, threshold):
    """
    Находит все пары объектов, у которых евклидово расстояние меньше threshold.
    
    Аргументы:
    X -- двумерный список чисел (n x m)
    threshold -- пороговое значение расстояния
    
    Возвращает:
    Список кортежей (i, j, distance), где i < j и distance < threshold
    """
    result = []
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            distance_sum = 0
    
            for k in range(len(X[i])):
                distance_sum += (X[i][k] - X[j][k]) ** 2

            distance = math.sqrt(distance_sum)

            if distance <= threshold:
                result.append((i, j, distance))

    return result 