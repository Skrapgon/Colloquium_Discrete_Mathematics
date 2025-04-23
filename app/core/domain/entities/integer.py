from dataclasses import dataclass

from core.domain.entities.natural import Natural

@dataclass
class Integer:
    """
    Класс, описывающий целые числа.

    Attributes:
        sign (int): Знак числа. 0 - положительное, 1 - отрицательное.
        number (Natural): Модуль числа.
    """
    
    sign: int
    number: Natural