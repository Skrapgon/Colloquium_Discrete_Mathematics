from re import fullmatch

from core.domain.exceptions.parsers import StrToRationalException
from core.service.parsers.natural_parser import NaturalParser
from core.service.parsers.integer_parser import IntegerParser
from core.domain.entities.rational import Rational
from core.service.parsers.regex_patters import RATIONAL_PATTERN

class RationalParser:
    def str_to_ratio(ratio_str: str) -> Rational:
        if not fullmatch(RATIONAL_PATTERN, ratio_str):
            raise StrToRationalException(ratio_str)
        slash_index = ratio_str.find('/')
        return Rational(IntegerParser.str_to_int(ratio_str[:slash_index]), NaturalParser.str_to_nat(ratio_str[slash_index+1::]))
        
    def ratio_to_str(ratio: Rational) -> str:
        return f'{IntegerParser.int_to_str(ratio.numerator)}/{NaturalParser.nat_to_str(ratio.denominator)}'