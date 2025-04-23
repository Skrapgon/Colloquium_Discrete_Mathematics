class FirstLessThanSecondException(Exception):
    """
    Исключение, вызываемое, когда первое число меньше второго.

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.message = f'Ошибка: первое число ({first}) меньше второго ({second}).'
        super().__init__(self.message)

class IncorrectDigitException(Exception):
    """
    Исключение, вызываемое, когда число не является цифрой.

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, digit):
        self.digit = digit
        self.message = f'Ошибка: число ({digit}) не является цифрой.'
        super().__init__(self.message)
      
class IncorrectDegreeException(Exception):
    """
    Исключение, вызываемое, когда число не является натуральной степенью 10.

    Attributes:
        message (str): Сообщение об ошибке.
    """
    
    def __init__(self, degree):
        self.degree = degree
        self.message = f'Ошибка: указанное число ({degree}) не является натуральной степенью 10.'
        super().__init__(self.message)
        
        
class ConvertNegativeToNaturalException(Exception):
    """
    Исключение, вызываемое при попытке преобразовать отрицательное число в натуральное.
    
    Attributes:
        message (str): Сообщение об ошибке
    """
    
    def __init__(self, integer):
        self.integer = integer
        self.message = f'Ошибка: число ({integer}) отрицательное.'
        super().__init__(self.message)