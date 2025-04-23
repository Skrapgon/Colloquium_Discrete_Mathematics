from re import fullmatch

from core.domain.exceptions.parsers import StrToPolymonialException
from core.service.parsers.rational_parser import RationalParser
from core.domain.entities.polynomial import Polynomial
from core.service.parsers.regex_patters import POLYNOMIAL_PATTERN

class PolynomialParser:
    
    def str_to_polynom(polynom_str: str) -> Polynomial:
        if not fullmatch(POLYNOMIAL_PATTERN, polynom_str):
            raise StrToPolymonialException(polynom_str)
        coef_str = polynom_str.split('; ')
        return Polynomial(len(coef_str)-1, [RationalParser.str_to_ratio(coef) for coef in coef_str])
    
    def polynom_to_str(polynom: Polynomial) -> str:
        return '; '.join(map(RationalParser.ratio_to_str, polynom.coefficients))