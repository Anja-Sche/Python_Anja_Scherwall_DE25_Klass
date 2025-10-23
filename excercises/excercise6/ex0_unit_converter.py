from numbers import Number
from utils import validate_positive_number

class UnitConverter:
    def __init__(self, value: Number):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value): #kan stå 'value' också
        #validation code
        validate_positive_number(new_value)

        self._value = new_value

    def inch_to_cm(self):
        return 2.54 * self.value

    def foot_to_meters(self):
        return .3048 * self.value
    

unit_converter = UnitConverter(5)

#shortcut to get this output:
# unit_converter.value = 5
#print(f"{unit_converter.value =}")



print(f"{unit_converter.foot_to_meters() =}")