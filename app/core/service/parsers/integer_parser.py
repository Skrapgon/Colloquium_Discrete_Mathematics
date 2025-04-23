from re import fullmatch

from core.domain.exceptions.parsers import StrToIntegerException
from core.service.parsers.natural_parser import NaturalParser
from core.domain.entities.integer import Integer
from core.service.parsers.regex_patters import INTEGER_PATTERN

class IntegerParser:
    
    def str_to_int(int_str: str) -> Integer:
        if not fullmatch(INTEGER_PATTERN, int_str):
            raise StrToIntegerException(int_str)
        
        return Integer(1, NaturalParser.str_to_nat(int_str[1::])) if int_str[0] == '-' else Integer(0, NaturalParser.str_to_nat(int_str))
    
    def int_to_str(integer: Integer) -> str:
        result = NaturalParser.nat_to_str(integer.number)
        if integer.sign:
            result = '-' + result
        return result