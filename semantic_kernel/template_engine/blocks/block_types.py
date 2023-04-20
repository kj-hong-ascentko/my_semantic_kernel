from enum import Enum, auto

class BlackTypes(Enum):
    UNDEFINED = auto()
    TEXT = auto()
    CODE = auto()
    VARIABLE = auto()
    VALUE = auto()
    FUNCTION_ID = auto()