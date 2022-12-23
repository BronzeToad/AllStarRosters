from enum import Enum


# ============================================================================ #

class EnvFile(Enum):
    SECRET = '.env'
    PYTHON = '.env-py'


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')