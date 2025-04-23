from copy import deepcopy

from core.domain.entities.integer import Integer
from core.domain.entities.natural import Natural
from core.domain.exceptions.numbers import ConvertNegativeToNaturalException
from core.service.parsers.integer_parser import IntegerParser
from core.service.solvers.natural_solver import ADD_NN_N, COM_NN_D, DIV_NN_N, MUL_NN_N, NZER_N_B, SUB_NN_N


def ABS_Z_N(integer: Integer) -> Natural:
    """
    Модуль целого числа.
    
    Args:
        integer (Integer): Целое число.
    
    Returns:
        Natural: Модуль числа.
    """
    
    return deepcopy(integer.number)


def POZ_Z_D(integer: Integer) -> int:
    """
    Вычисление знака целого числа.
    
    Args:
        integer (Integer): Целое число.
    
    Returns:
        int: Знак числа. 0 - Число равно 0, 1 - Число отрицательное, 2 - Число положительное.
    """
    if NZER_N_B(integer.number):
        if integer.sign == 0:
            return 2
        else:
            return 1
    
    return 0


def MUL_ZM_Z(integer: Integer) -> Integer:
    """
    Изменение знака на противоположный у целого числа.
    
    Args:
        integer (Integer): Целое число.
    
    Returns:
        Integer: Число с инверсированным знаком.
    """
    result = deepcopy(integer)
    if POZ_Z_D(result):
        result.sign ^= 1
        
    return result


def TRANS_N_Z(nat: Natural) -> Integer:
    """
    Преобразование натурального числа в целое.
    
    Args:
        nat (Natural): Натуральное число.
    
    Returns:
        Integer: Преобразованное в целое натуральное число.
    """
    
    return Integer(0, deepcopy(nat))


def TRANS_Z_N (integer: Integer) -> Natural:
    """
    Преобразование целого числа в натуральное.
    
    Args:
        integer (Integer): Целое число.
    
    Returns:
        Natural: Преобразованное в натуральное целое число.
    """
    
    if POZ_Z_D(integer) == 1:
        raise ConvertNegativeToNaturalException(IntegerParser.int_to_str(integer))
    
    return deepcopy(integer.number)


def ADD_ZZ_Z(integer1: Integer, integer2: Integer) -> Integer:
    """
    Сложение двух целых чисел.
    
    Args:
        integer1 (Integer): Первое целое число.
        integer2 (Integer): Второе целое число.
        
    Returns:
        Integer: Сумма двух целых чисел.
    """
    
    int1_copy = deepcopy(integer1)
    int2_copy = deepcopy(integer2)
    if COM_NN_D(ABS_Z_N(int1_copy), ABS_Z_N(int2_copy)) == 1:
        int2_copy, int1_copy = int1_copy, int2_copy
    
    poz1 = POZ_Z_D(int1_copy)
    poz2 = POZ_Z_D(int2_copy)
    if poz1 == poz2:
        return Integer(int1_copy.sign, ADD_NN_N(ABS_Z_N(int1_copy), ABS_Z_N(int2_copy)))
    elif poz2 == 0:
        return int1_copy
    else:
        return Integer(int1_copy.sign, SUB_NN_N(ABS_Z_N(int1_copy), ABS_Z_N(int2_copy)))
    
    
def SUB_ZZ_Z(integer1: Integer, integer2: Integer) -> Integer:
    """
    Вычитание двух целых чисел.
    
    Args:
        integer1 (Integer): Первое целое число.
        integer2 (Integer): Второе целое число.
        
    Returns:
        Integer: Разность двух целых чисел.
    """
    
    return ADD_ZZ_Z(integer1, MUL_ZM_Z(integer2))


def MUL_ZZ_Z(integer1: Integer, integer2: Integer) -> Integer:
    """
    Умножение двух целых чисел.
    
    Args:
        integer1 (Integer): Первое целое число.
        integer2 (Integer): Второе целое число.
        
    Returns:
        Integer: Произведение двух целых чисел.
    """
    
    int1_copy = deepcopy(integer1)
    int2_copy = deepcopy(integer2)
    if COM_NN_D(ABS_Z_N(int1_copy), ABS_Z_N(int2_copy)) == 1:
        int2_copy, int1_copy = int1_copy, int2_copy
    
    poz1 = POZ_Z_D(int1_copy)
    poz2 = POZ_Z_D(int2_copy)
    if poz2 == 0:
        return int2_copy
    elif poz1 == poz2:
        return Integer(0, MUL_NN_N(ABS_Z_N(int1_copy), ABS_Z_N(int2_copy)))
    else:
        return Integer(1, MUL_NN_N(ABS_Z_N(int1_copy), ABS_Z_N(int2_copy)))
    
    
def DIV_ZZ_Z(integer1: Integer, integer2: Integer) -> Integer:
    """
    Целочисленное деление двух целых чисел.
    
    Args:
        integer1 (Integer): Первое целое число.
        integer2 (Integer): Второе целое число.
        
    Returns:
        Integer: Частное от целочисленного деления двух целых чисел.
    """
    
    result = Integer(0, DIV_NN_N(ABS_Z_N(integer1), ABS_Z_N(integer2)))
    if POZ_Z_D(result) == 0:
        return result
    if POZ_Z_D(integer1) != POZ_Z_D(integer2):
        result = ADD_ZZ_Z(result, Integer(0, Natural(1, [1])))
        result = MUL_ZM_Z(result)
    
    return result

    
def MOD_ZZ_Z(integer1: Integer, integer2: Integer) -> Integer:
    """
    Деление с остатком двух целых чисел.
    
    Args:
        integer1 (Integer): Первое целое число.
        integer2 (Integer): Второе целое число.
        
    Returns:
        Integer: Остаток от целочисленного деления двух целых чисел.
    """
    
    div = DIV_ZZ_Z(integer1, integer2)
    mul = MUL_ZZ_Z(div, integer2)
    return SUB_ZZ_Z(integer1, mul)