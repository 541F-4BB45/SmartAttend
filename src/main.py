from pathlib import Path


def createClass(user_name: str, class_name: str, quantity: int) -> None:


    # Input validation

    if not user_name or not class_name or not quantity:
        raise ValueError('A null value was input!')
    
    if user_name.isspace() or class_name.isspace():
        raise ValueError('The input class or username was all spaces')
    
    if not user_name.isalpha():
        raise ValueError('The username was in the wrong format')
    
    if not class_name.isalpha():
        raise ValueError('The classname was in the wrong format')
    
    if quantity <= 0:
        raise ValueError('The input quantity was an invalid amount')
    

    # Actual working

    base_path: Path = Path(f'C:\\{user_name}\\{class_name}')
    base_path.mkdir(parents=True, exist_ok=True)

    for i in range(quantity):

        directories_path: Path = base_path / str(i + 1)
        directories_path.mkdir(parents=True, exist_ok=True)


def login(user_name: str, password: str) -> None:

    