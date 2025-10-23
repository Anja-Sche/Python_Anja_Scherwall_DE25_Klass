from numbers import Number

def validate_positive_number(value) -> None:
    if not isinstance(value, Number):
        raise TypeError(f"Your value must ba a number, not {type(value)}")
    
    if value < 0:
        raise ValueError(f"value can't be negative, not {value}")