from copy import deepcopy

from core.domain.entities.natural import Natural
from core.domain.exceptions.numbers import FirstLessThanSecondException, IncorrectDegreeException, IncorrectDigitException
from core.service.parsers.natural_parser import NaturalParser


def COM_NN_D(nat1: Natural, nat2: Natural) -> int:
    """
    Сравнение 2 чисел.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        int: номер меньшего числа, 0 для равных чисел.
    """
    
    if nat1.digit_count > nat2.digit_count:
        return 2
    elif nat1.digit_count < nat2.digit_count:
        return 1
    
    for i in range(nat1.digit_count):
        if nat1.digits[i] > nat2.digits[i]:
            return 2
        elif nat1.digits[i] < nat2.digits[i]:
            return 1
    return 0


def NZER_N_B(nat: Natural) -> bool:
    """
    Проверка, что число не равно 0.
    
    Args:
        nat (Natural): Число.
        
    Returns:
        bool: неравенство числа 0.
    """
    
    return nat.digits[0] != 0


def ADD_1N_N(nat: Natural) -> Natural:
    """
    Добавление к числу единицы.
    
    Args:
        nat (Natural): Число.
        
    Returns:
        Natural: Число, увеличенное на единицу.
    """
    result = deepcopy(nat)
    
    i = result.digit_count - 1
    
    while i > 0 and result.digits[i] == 9:
        result.digits[i] = 0
        i -= 1
    
    result.digits[i] += 1
    if result.digits[0] == 10:
        result.digits[0] = 0
        result.digits.insert(0, 1)
        result.digit_count += 1
    
    return result


def ADD_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Сложение двух натуральных чисел.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: Сумма двух чисел.
    """
    
    result = deepcopy(nat1)
    nat2_copy = deepcopy(nat2)
    
    if COM_NN_D(result, nat2_copy) < 2:
        result, nat2_copy = nat2_copy, result
    
    if NZER_N_B(nat2):
        remain = 0
        for i in range(nat2_copy.digit_count):
            result.digits[-i-1] += nat2_copy.digits[-i-1] + remain
            remain = result.digits[-i-1] // 10
            result.digits[-i-1] %= 10
            
        cur_digit = result.digit_count - nat2_copy.digit_count - 1
        while remain and cur_digit >= 0:
            result.digits[cur_digit] += remain
            remain = result.digits[cur_digit] // 10
            result.digits[cur_digit] %= 10
            cur_digit -= 1
            
        if remain:
            result.digit_count += 1
            result.digits.insert(0, remain)
    
    return result


def SUB_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Вычитание из первого числа второго. Первое число должно быть не меньше второго.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: Разность двух чисел.
    """
    
    comm_nn_d = COM_NN_D(nat1, nat2)
    
    if comm_nn_d == 1:
        raise FirstLessThanSecondException(NaturalParser.nat_to_str(nat1), NaturalParser.nat_to_str(nat2))
    elif comm_nn_d == 0:
        return NaturalParser.str_to_nat('0')
    
    result = deepcopy(nat1)
    if NZER_N_B(nat2):
        zero_count = -1
        
        for i in range(1, result.digit_count+1):
            if i < nat2.digit_count+1:
                result.digits[-i] -= nat2.digits[-i]
                
            if result.digits[-i] < 0:
                result.digits[-i] += 10
                result.digits[-i-1] -= 1
            
            zero_count = max(result.digit_count-i+1, zero_count) if result.digits[-i] == 0 else -1
            
        if zero_count != -1:
            result.digit_count -= zero_count
            result.digits = result.digits[zero_count::]
            
    return result


def MUL_ND_N(nat: Natural, multiplier: int) -> Natural:
    """
    Умножение числа на цифру.
    
    Args:
        nat (Natural): Число.
        multiplier (int): Цифра множитель.
    
    Returns:
        Natural: Произведение числа и цифры.
    """
    
    if multiplier == 0 or not NZER_N_B(nat):
        return NaturalParser.str_to_nat('0')
    elif 10 > multiplier > 0:
        result = deepcopy(nat)
        overflow = 0
        
        for i in range(result.digit_count):
            result.digits[-i-1] = result.digits[-i-1] * multiplier + overflow
            result.digits[-i-1], overflow = result.digits[-i-1] % 10, result.digits[-i-1] // 10
            
        if overflow:
            result.digit_count += 1
            result.digits.insert(0, overflow)
            
        return result
    else:
        raise IncorrectDigitException(multiplier)
    

def MUL_Nk_N (nat: Natural, k: int) -> Natural:
    """
    Умножение числа на неотрицательную степень 10.
    
    Args:
        nat (Natural): Число.
        multiplier (int): неотрицательная степень 10.
    
    Returns:
        Natural: Произведение числа и 10^k.
    """
    
    if k < 0:
        raise IncorrectDegreeException(k)
    
    result = deepcopy(nat)
    if NZER_N_B(result):
        result.digit_count += k
        result.digits.extend([0 for _ in range(k)])
        
    return result


def MUL_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Умножение двух натуральных чисел.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: Произведение двух чисел.
    """
    
    nat1_copy = deepcopy(nat1)
    nat2_copy = deepcopy(nat2)
    
    if COM_NN_D(nat1_copy, nat2_copy) < 2:
        nat1_copy, nat2_copy = nat2_copy, nat1_copy
        
    if not NZER_N_B(nat2_copy):
        return nat2_copy
    
    result = NaturalParser.str_to_nat('0')
    for i in range(nat2_copy.digit_count):
        tmp = MUL_ND_N(nat1_copy, nat2_copy.digits[nat2_copy.digit_count-i-1])
        tmp = MUL_Nk_N(tmp, i)
        result = ADD_NN_N(result, tmp)
    
    return result


def SUB_NDN_N(nat1: Natural, nat2: Natural, multiplier: int) -> Natural:
    """
    Вычитание из первого числа второго, унможенного на цифру. Первое число должно быть не меньше второго, умноженного на цифру.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
        multiplier (int): Цифра множитель.
    
    Returns:
        Natural: Разность первого числа и произведения второго и цифры.
    """
    
    new_nat2 = MUL_ND_N(nat2, multiplier)
    return SUB_NN_N(nat1, new_nat2)


def DIV_NN_Dk(nat1: Natural, nat2: Natural) -> Natural:
    """
    Вычисление первой цифры от деления первого числа на второе, домноженной на 10^k,где k - номер позиции этой цифры в частном (номер считается с нуля справа-налево).
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: Первая цифра деления первого числа на второе, домноженная на 10^k.
    """
    
    if not NZER_N_B(nat2):
        raise ZeroDivisionError('Ошибка: Деление на 0 невозможно')
    
    result = NaturalParser.str_to_nat('0')
    deg = 0
    tmp = nat2
    while COM_NN_D(nat1, tmp) != 1:
        deg += 1
        tmp = MUL_Nk_N(tmp, 1)
        
    if deg:
        if COM_NN_D(nat1, tmp) == 1:
            deg -= 1
            tmp.digit_count -= 1
            tmp.digits.pop()
            
        sub = deepcopy(nat1)
        while COM_NN_D(sub, tmp) != 1:
            sub = SUB_NN_N(sub, tmp)
            result = ADD_1N_N(result)
        result = MUL_Nk_N(result, deg)
        
    return result


def DIV_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Целочисленное деление первого числа на второе.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: Частное от целочисленного деления двух чисел.
    """
    
    result = NaturalParser.str_to_nat('0')
    nat1_copy = deepcopy(nat1)
    while COM_NN_D(nat1_copy, nat2) != 1:
        tmp = DIV_NN_Dk(nat1_copy, nat2)
        nat1_copy = SUB_NN_N(nat1_copy, MUL_NN_N(tmp, nat2))
        result = ADD_NN_N(result, tmp)
    
    return result


def MOD_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Деление с остатком первого числа на второе.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: Остаток от целочисленного деления двух чисел.
    """
    
    div = DIV_NN_N(nat1, nat2)
    mul = MUL_NN_N(div, nat2)
    return SUB_NN_N(nat1, mul)


def GCF_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Вычисление НОД (наибольший общий делитель) через алгоритм Евклида.
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: НОД двух чисел.
    """
    
    if not NZER_N_B(nat1) and not NZER_N_B(nat2):
        raise ZeroDivisionError('Ошибка: НОД для двух нулей неопределен.')
    
    nat1_copy = deepcopy(nat1)
    nat2_copy = deepcopy(nat2)
    
    while NZER_N_B(nat1_copy) and NZER_N_B(nat2_copy):
        if COM_NN_D(nat1_copy, nat2_copy) == 2:
            nat1_copy = MOD_NN_N(nat1_copy, nat2_copy)
        else:
            nat2_copy = MOD_NN_N(nat2_copy, nat1_copy)
    
    return ADD_NN_N(nat1_copy, nat2_copy)


def LCM_NN_N(nat1: Natural, nat2: Natural) -> Natural:
    """
    Вычисление НОК (наименьшее общее кратное).
    
    Args:
        nat1 (Natural): Первое число.
        nat2 (Natural): Второе число.
    
    Returns:
        Natural: НОК двух чисел.
    """
    
    if not NZER_N_B(nat1) or not NZER_N_B(nat2):
        raise ZeroDivisionError('Ошибка: Невозможно вычислить НОК для 0')
    
    gcf = GCF_NN_N(nat1, nat2)
    nat1_div = DIV_NN_N(nat1, gcf)
    nat2_div = DIV_NN_N(nat2, gcf)
    return MUL_NN_N(gcf, MUL_NN_N(nat1_div, nat2_div))