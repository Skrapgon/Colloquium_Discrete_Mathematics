from copy import deepcopy

from core.domain.entities.polynomial import Polynomial
from core.domain.entities.rational import Rational
from core.service.parsers.integer_parser import IntegerParser
from core.service.parsers.polynoial_parser import PolynomialParser
from core.service.parsers.rational_parser import RationalParser
from core.service.solvers.natural_solver import GCF_NN_N, LCM_NN_N
from core.service.solvers.integer_solver import ABS_Z_N, POZ_Z_D, TRANS_N_Z
from core.service.solvers.rational_solver import ADD_QQ_Q, DIV_QQ_Q, MUL_QQ_Q, SUB_QQ_Q, TRANS_Z_Q


def dec_d_p(polynom: Polynomial) -> Polynomial:
    """
    Понижение степени полинома, если при старших степенях 0.
    
    Args:
        polynom (Polynomial): Полином.
    
    Returns:
        Polynomial: Полином с пониженной степенью (если есть нулевые старшие коэффициенты).
    """
    
    pol = deepcopy(polynom)
    
    c = 0
    while c != pol.polynom_degree and POZ_Z_D(pol.coefficients[c].numerator) == 0:
        c += 1
        
    pol.polynom_degree -= c
    pol.coefficients = pol.coefficients[c::]
        
    return pol


def ADD_PP_P(polynom1: Polynomial, polynom2: Polynomial) -> Polynomial:
    """
    Сложение полиномов.
    
    Args:
        polynom1 (Polynomial): Первый полином.
        polynom2 (Polynomial): Второй полином.
    
    Returns:
        Polynomial: Сумма полиномов.
    """
    
    pol1 = dec_d_p(polynom1)
    pol2 = dec_d_p(polynom2)
    
    if pol1.polynom_degree < pol2.polynom_degree:
        pol1, pol2 = pol2, pol1
        
    for i in range(pol2.polynom_degree+1):
        pol1.coefficients[-i-1] = ADD_QQ_Q(pol1.coefficients[-i-1], pol2.coefficients[-i-1])
        
    return dec_d_p(pol1)


def SUB_PP_P(polynom1: Polynomial, polynom2: Polynomial) -> Polynomial:
    """
    Вычитание полиномов.
    
    Args:
        polynom1 (Polynomial): Первый полином.
        polynom2 (Polynomial): Второй полином.
    
    Returns:
        Polynomial: Разность полиномов.
    """
    
    pol1 = dec_d_p(polynom1)
    pol2 = dec_d_p(polynom2)
    
    if pol1.polynom_degree < pol2.polynom_degree:
        pol1, pol2 = pol2, pol1
        
    for i in range(pol2.polynom_degree+1):
        pol1.coefficients[-i-1] = SUB_QQ_Q(pol1.coefficients[-i-1], pol2.coefficients[-i-1])
    
    return dec_d_p(pol1)


def MUL_PQ_P(polynom: Polynomial, ratio: Rational) -> Polynomial:
    """
    Умножение полинома на рациональное число.
    
    Args:
        polynom (Polynomial): Полином.
        ratio (Rational): Рациональное число.
    
    Returns:
        Polynomial: Произведение полинома и рационального числа.
    """
    
    if POZ_Z_D(ratio.numerator) == 0:
        return PolynomialParser.str_to_polynom('0/1')
    
    result = dec_d_p(polynom)
    for i in range (result.polynom_degree+1):
        result.coefficients[i] = MUL_QQ_Q(result.coefficients[i], ratio)
    return dec_d_p(result)


def MUL_Pxk_P(polynom: Polynomial, k: int) -> Polynomial:
    """
    Умножение полинома на x^k.
    
    Args:
        polynom (Polynomial): Полином.
        k (int): степень x.
    
    Returns:
        Polynomial: Произведение полинома на x^k.
    """
    
    result = dec_d_p(polynom)
    
    result.polynom_degree += k
    result.coefficients.extend([RationalParser.str_to_ratio('0/1') for _ in range(k)])
    return dec_d_p(result)


def LED_P_Q(polynom: Polynomial) -> Rational:
    """
    Вычисление старшего коэффициента полинома.
    
    Args:
        polynom (Polynomial): Полином.
    
    Returns:
        Rational: Старший коэффициент полинома.
    """
    
    return dec_d_p(polynom).coefficients[0]


def DEG_P_N(polynom: Polynomial) -> int:
    """
    Вычисление степени полинома.
    
    Args:
        polynom (Polynomial): Полином.
    
    Returns:
        int: Степень полинома.
    """
    
    return dec_d_p(polynom).polynom_degree


def FAC_P_Q (polynom: Polynomial) -> Rational:
    """
    Вычисление НОД среди числителей и НОК среди знаменателей коэффициентов полинома.
    
    Args:
        polynom (Polynomial): Полином.
    
    Returns:
        Rational: НОД/НОК без сокращения.
    """
    
    pol = dec_d_p(polynom)
    
    deg = pol.polynom_degree
    
    gcf = ABS_Z_N(pol.coefficients[deg].numerator)
    lcm = deepcopy(pol.coefficients[deg].denominator)
    
    for i in range(deg):
        gcf = GCF_NN_N(gcf, ABS_Z_N(pol.coefficients[i].numerator))
        lcm = LCM_NN_N(lcm, pol.coefficients[i].denominator)
    
    return Rational(TRANS_N_Z(gcf), lcm)


def MUL_PP_P(polynom1: Polynomial, polynom2: Polynomial) -> Polynomial:
    """
    Умножение двух полиномов.
    
    Args:
        polynom1 (Polynomial): Первый полином.
        polynom2 (Polynomial): Второй полином.
    
    Returns:
        Polynomial: Произведение полиномов.
    """
    
    result = PolynomialParser.str_to_polynom('0/1')
    
    pol1 = dec_d_p(polynom1)
    pol2 = dec_d_p(polynom2)
    
    if POZ_Z_D(pol1.coefficients[0].numerator) and POZ_Z_D(pol2.coefficients[0].numerator):
        for i in range(pol1.polynom_degree+1):
            summ = MUL_PQ_P(pol1, pol2.coefficients[pol2.polynom_degree-i])
            summ = MUL_Pxk_P(summ, pol2.polynom_degree-i)
            result = ADD_PP_P(result, summ)
        
    return dec_d_p(result)


def DIV_PP_P(polynom1: Polynomial, polynom2: Polynomial) -> Polynomial:
    """
    Деление двух полиномов.
    
    Args:
        polynom1 (Polynomial): Первый полином.
        polynom2 (Polynomial): Второй полином.
    
    Returns:
        Polynomial: Частное от деления полиномов.
    """
    
    pol1 = dec_d_p(polynom1)
    pol2 = dec_d_p(polynom2)
    
    result = PolynomialParser.str_to_polynom('0/1')
    
    while pol1.polynom_degree >= pol2.polynom_degree:
        div = DIV_QQ_Q(pol1.coefficients[0], pol2.coefficients[0])
        k = pol1.polynom_degree - pol2.polynom_degree
        tmp = Polynomial(0, div)
        tmp = MUL_Pxk_P(tmp, k)
        result = ADD_PP_P(result, tmp)
        pol1 = SUB_PP_P(pol1, tmp)
    
    return result


def MOD_PP_P(polynom1: Polynomial, polynom2: Polynomial) -> Polynomial:
    """
    Нахождение остатка от деления двух полиномов.
    
    Args:
        polynom1 (Polynomial): Первый полином.
        polynom2 (Polynomial): Второй полином.
    
    Returns:
        Polynomial: Остаток от деления полиномов.
    """
    
    div = DIV_PP_P(polynom1, polynom2)
    
    return SUB_PP_P(polynom1, MUL_PP_P(div, polynom2))


def GCF_PP_P(polynom1: Polynomial, polynom2: Polynomial) -> Polynomial:
    """
    Вычисление НОД двух полиномов.
    
    Args:
        polynom1 (Polynomial): Первый полином.
        polynom2 (Polynomial): Второй полином.
        
    Returns:
        Polynomial: НОД полиномов.
    """
    
    divid = dec_d_p(polynom1)
    divis = dec_d_p(polynom2)
    
    divis = MOD_PP_P(divid, divis)
    while POZ_Z_D(divis.coefficients[0].numerator):
        divis, divid = divid, divis
        divis = MOD_PP_P(divid, divis)
    return divis


def DER_P_P(polynom: Polynomial) -> Polynomial:
    """
    Вычисление производной полинома.
    
    Args:
        polynom (Polynomial): Полином.
    
    Returns:
        Polynomial: Производная полинома.
    """
    
    result = deepcopy(polynom)
    
    for i in range(result.polynom_degree):
        mul = IntegerParser.str_to_int(str(result.polynom_degree-i))
        result.coefficients[i] = MUL_QQ_Q(result.coefficients[i], TRANS_Z_Q(mul))
        
    result.polynom_degree -= 1
    result.coefficients.pop()
    
    return result


def NMR_P_P(polynom: Polynomial) -> Polynomial:
    """
    Упрощение полинома: устранение кратных корней и нормализация.
    
    Args:
        polynom (Polynomial): Полином.
    
    Returns:
        Polynomial: Упрощенный полином.
    """
    
    pol = dec_d_p(polynom)
    
    der = DER_P_P(pol)
    nod = GCF_PP_P(pol, der)
    result = DIV_PP_P(pol, nod)
    norm_mul = DIV_QQ_Q(RationalParser.str_to_ratio('1/1'), result.coefficients[0])
    return MUL_PQ_P(norm_mul)