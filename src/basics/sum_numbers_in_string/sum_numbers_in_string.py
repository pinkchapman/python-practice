import re

def sum_numbers_in_string(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    total = 0
    number = ""
    for i in input_string:
        if i.isdigit():
            number += i
        else:
            if number != "":
                total += int(number)
                number = ""
    if number != "":
        total += int(number)
    return total              

def sum_numbers_in_string_regex(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
 