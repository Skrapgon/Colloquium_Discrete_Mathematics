class StrToNaturalException(Exception):
    """
    Исключение, вызываемое, когда вводимая строка не соответствует натуральному числу или 0 (число с ведущими нулями также считается недопустимым).

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, nat_str):
        self.nat_str = nat_str
        self.message = f'Ошибка: Строка {nat_str} не содержит натуральное число или 0.'
        super().__init__(self.message)

class StrToIntegerException(Exception):
    """
    Исключение, вызываемое, когда вводимая строка не соответствует целому числу.

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, int_str):
        self.int_str = int_str
        self.message = f'Ошибка: Строка {int_str} не содержит целое число.'
        super().__init__(self.message)
    
class StrToRationalException(Exception):
    """
    Исключение, вызываемое, когда вводимая строка не соответствует рациональной дроби.

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, ratio_str):
        self.ratio_str = ratio_str
        self.message = f'Ошибка: Строка {ratio_str} не содержит рациональную дробь.'
        super().__init__(self.message)
    
class StrToPolymonialException(Exception):
    """
    Исключение, вызываемое, когда вводимая строка не соответствует полиному.

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, polynom_str):
        self.polynom_str = polynom_str
        self.message = f'Ошибка: Строка {polynom_str} не является полиномом.'
        super().__init__(self.message)