from dataclasses import dataclass

from core.domain.entities.integer import Integer
from core.domain.entities.natural import Natural

@dataclass
class Rational:
    """
    Класс, описывающий рациональную дробь.

    Attributes:
        numerator (Integer): Числитель.
        denominator (Natural): Знаменатель.
    """
    
    numerator: Integer
    denominator: Natural