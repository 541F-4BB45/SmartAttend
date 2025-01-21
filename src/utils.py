from typing import Union
from icecream import ic

def validateInput(**kwargs: Union[str, int, float]) -> None:

    # Checking for null values
    for variable in kwargs.keys():
        # ic(variable)
        # ic(type(variable))
        if not variable:
            raise ValueError('One of the inputs in the function was null')
        
    # Checking for spaces (only for strings)
    for key, value in kwargs.items():
        ic(key)
        ic(value)
        if isinstance(value, str) and value.isspace():
            raise ValueError(f'Input for key "{key}" is only spaces')
    
    # Checking for correct datatypes
    for variable, datatype in kwargs.items():
        if not isinstance(variable, datatype):
            raise TypeError('One of the inputs in the function was not of the right type')
        
    # # Checking for correct format
    # for variable, value in kwargs.items():
    #     _, format = value

    #     if format == 'alpha':
    #         if not variable.isalpha():
    #             raise TypeError('Input was not alpha')
    #     if format == 'num':
    #         if not variable.isnumeric():
    #             raise TypeError('Input was not num')
    #     if format == 'alnum':
    #         if not variable.isalnum():
    #             raise TypeError('Input was not alnum')
    # {variable: type}

name = None
validateInput(name=str)

# {name : (type, format)}