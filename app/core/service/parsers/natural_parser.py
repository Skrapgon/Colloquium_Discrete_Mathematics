from re import fullmatch

from core.domain.exceptions.parsers import StrToNaturalException
from core.domain.entities.natural import Natural
from core.service.parsers.regex_patters import NATURAL_PATTERN

class NaturalParser:
    
    def str_to_nat(nat_str: str) -> Natural:
        if not fullmatch(NATURAL_PATTERN, nat_str):
            raise StrToNaturalException(nat_str)
        return Natural(len(nat_str), [int(c) for c in nat_str])
        
    def nat_to_str(nat: Natural) -> str:
        return ''.join(map(str, nat.digits))