from enum import Enum, auto


# ============================================================================ #

class EnvFile(Enum):
    SECRET = '.env'
    PYTHON = '.env-py'


class ProgrammingCase(Enum):
    CAMEL = auto()      # camelCase
    COBOL = auto()      # COBOL-CASE
    FLAT = auto()       # flatcase
    KEBAB = auto()      # kebab-case
    PASCAL = auto()     # PascalCase
    SCREAM = auto()     # SCREAM_CASE
    SNAKE = auto()      # snake_case

# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')
