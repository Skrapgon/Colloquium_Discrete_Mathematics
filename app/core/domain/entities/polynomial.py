from dataclasses import dataclass
from typing import List

from core.domain.entities.rational import Rational

@dataclass
class Polynomial:
    """
    Класс, описывающий полином натуральной степени с рациональными коэффициентами.

    Attributes:
        polynom_degree (int): Степень полинома.
        coefficients (List[Rational]): Коэффициенты полинома.
    """
    
    polynom_degree: int
    coefficients: List[Rational]