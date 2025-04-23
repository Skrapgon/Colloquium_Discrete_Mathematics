from dataclasses import dataclass
from typing import List

@dataclass
class Natural:
    """
    Класс, описывающий натуральные числа и 0.

    Attributes:
        digit_count (int): Количество разрядов числа.
        digits (List[int]): Само число.
    """
    
    digit_count: int
    digits: List[int]