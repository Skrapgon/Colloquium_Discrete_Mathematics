from copy import deepcopy

from core.domain.entities.integer import Integer
from core.domain.entities.rational import Rational
from core.domain.exceptions.numbers import RationalIsNotIntegerException
from core.service.parsers.integer_parser import IntegerParser
from core.service.parsers.natural_parser import NaturalParser
from core.service.solvers.integer_solver import ABS_Z_N, ADD_ZZ_Z, DIV_ZZ_Z, MUL_ZM_Z, MUL_ZZ_Z, POZ_Z_D, TRANS_N_Z
from core.service.solvers.natural_solver import COM_NN_D, DIV_NN_N, GCF_NN_N, LCM_NN_N, MUL_NN_N, NZER_N_B


def RED_Q_Q(ratio: Rational) -> Rational:
    """
    Сокращение рациональной дроби.
    
    Args:
        ratio (Rational): Рациональная дробь.
    
    Returns:
        Rational: Сокращенная рациональная дробь.
    """
    
    if not NZER_N_B(ratio.denominator):
        raise ZeroDivisionError('Ошибка: Знаменатель равен 0')
    
    gcf_n = GCF_NN_N(ABS_Z_N(ratio.numerator), ratio.denominator)
    gcf_z = TRANS_N_Z(gcf_n)
    new_numerator = DIV_ZZ_Z(ratio.numerator, gcf_z)
    if POZ_Z_D(ratio.numerator) != POZ_Z_D(gcf_z) and POZ_Z_D(ratio.numerator) != 0:
        new_numerator = ADD_ZZ_Z(new_numerator, IntegerParser.str_to_int('1'))
    
    return Rational(new_numerator, DIV_NN_N(ratio.denominator, gcf_n))


def INT_Q_B(ratio: Rational) -> bool:
    """
    Проверка, что рациональная дробь является целым числом.
    
    Args:
        ratio (Rational): Рациональная дробь.
    
    Returns:
        bool: Рациональная дробь является целым числом.
    """
    
    red_ratio = RED_Q_Q(ratio)
    if COM_NN_D(red_ratio.denominator, NaturalParser.str_to_nat('1')) == 0:
        return True
    return False


def TRANS_Z_Q(integer: Integer) -> Rational:
    """
    Преобразование целого числа в рациональное.
    
    Args:
        integer (Integer): Целое число.
        
    Returns:
        Rational: Целое число, преобразованное в рациональное.
    """
    
    int_copy = deepcopy(integer)
    return Rational(int_copy, NaturalParser.str_to_nat('1'))


def TRANS_Q_Z(ratio: Rational):
    """
    Преобразование рациональное дроби в целое число.
    
    Args:
        ratio (Rational): Рациональная дробь.
        
    Returns:
        Integer: рациональная дробь, преобразованная в целое число.
    """
    
    if INT_Q_B(ratio):
        return RED_Q_Q(ratio).numerator
    raise RationalIsNotIntegerException(ratio)


def ADD_QQ_Q(ratio1: Rational, ratio2: Rational) -> Rational:
    """
    Сложение двух рациональных дробей.
    
    Args:
        ratio1 (Rational): Первая рациональная дробь.
        ratio2 (Rational): Вторая рациональная дробь.
        
    Returns:
        Rational: Сумма дробей.
    """
    
    ra1 = RED_Q_Q(ratio1)
    ra2 = RED_Q_Q(ratio2)
    den = LCM_NN_N(ra1.denominator, ra2.denominator)
    
    dopmul1 = TRANS_N_Z(DIV_NN_N(den, ra1.denominator))
    dopmul2 = TRANS_N_Z(DIV_NN_N(den, ra2.denominator))
    
    numer = ADD_ZZ_Z(MUL_ZZ_Z(ratio1.numerator, dopmul1), MUL_ZZ_Z(ratio2.numerator, dopmul2))
    
    return RED_Q_Q(Rational(numer, den))


def SUB_QQ_Q(ratio1: Rational, ratio2: Rational) -> Rational:
    """
    Вычитание двух рациональных дробей.
    
    Args:
        ratio1 (Rational): Первая рациональная дробь.
        ratio2 (Rational): Вторая рациональная дробь.
        
    Returns:
        Rational: Разность дробей.
    """
    
    ra2 = Rational(MUL_ZM_Z(ratio2.numerator), deepcopy(ratio2.denominator))
    return ADD_QQ_Q(ratio1, ra2)


def MUL_QQ_Q(ratio1: Rational, ratio2: Rational) -> Rational:
    """
    Перемножение двух рациональных дробей.
    
    Args:
        ratio1 (Rational): Первая рациональная дробь.
        ratio2 (Rational): Вторая рациональная дробь.
        
    Returns:
        Rational: Произведение дробей.
    """
    
    ra1 = RED_Q_Q(ratio1)
    ra2 = RED_Q_Q(ratio2)
    
    result = Rational(MUL_ZZ_Z(ra1.numerator, ra2.numerator), MUL_NN_N(ra1.denominator, ra2.denominator))
    return RED_Q_Q(result)


def DIV_QQ_Q(ratio1: Rational, ratio2: Rational) -> Rational:
    """
    Деление двух рациональных дробей.
    
    Args:
        ratio1 (Rational): Первая рациональная дробь.
        ratio2 (Rational): Вторая рациональная дробь.
        
    Returns:
        Rational: Частное дробей.
    """
    
    numer = TRANS_N_Z(ratio2.denominator)
    if POZ_Z_D(ratio2.numerator) == 1:
        numer = MUL_ZM_Z(numer)
    denom = ABS_Z_N(ratio2.numerator)
    
    ra2 = Rational(numer, denom)
    return MUL_QQ_Q(ratio1, ra2)