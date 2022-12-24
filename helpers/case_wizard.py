import numpy as np
from icecream import ic
from helpers.enum_factory import ProgrammingCase


# ============================================================================ #

class CaseWizard:

    def __init__(self,
                 input_string: str,
                 convert_to: ProgrammingCase,
                 input_case: ProgrammingCase):  # FIXME: remove after finishing detect_case()

        self.input_string = input_string
        self.convert_to = convert_to
        self.input_case = input_case    # FIXME: remove after finishing detect_case()
        # self.input_case = self.detect_case(self.input_string)

    # ============================================================================ #

    @property
    def input_string(self) -> str:
        return self._input_string

    @input_string.setter
    def input_string(self, val):
        self._input_string = str(val).replace('__', '_').strip()

    @property
    def convert_to(self) -> ProgrammingCase:
        return self._convert_to

    @convert_to.setter
    def convert_to(self, val):
        self._convert_to = val

    @property   # FIXME: remove after finishing detect_case()
    def input_case(self) -> ProgrammingCase:
        return self._input_case

    @input_case.setter  # FIXME: remove after finishing detect_case()
    def input_case(self, val):
        self._input_case = val

    # ============================================================================ #

    @staticmethod
    def detect_case(input_string: str) -> ProgrammingCase:
        pass    # TODO

    def is_camel_case(self) -> bool:
        pass    # TODO

    def is_cobol_case(self) -> bool:
        pass    # TODO

    def is_flat_case(self) -> bool:
        pass    # TODO

    def is_kebab_case(self) -> bool:
        pass    # TODO

    def is_pascal_case(self) -> bool:
        pass    # TODO

    def is_scream_case(self) -> bool:
        pass    # TODO

    def is_snake_case(self) -> bool:
        pass    # TODO

    # ============================================================================ #

    @classmethod
    def convert_case(cls,
                     input_string: str,
                     convert_to: ProgrammingCase,
                     input_case: ProgrammingCase):  # FIXME: remove after finishing detect_case()

        # wiz = cls(input_string, convert_to)
        wiz = cls(input_string, convert_to, input_case)     # FIXME: remove after finishing detect_case()

        con = [
            input_string == ProgrammingCase.CAMEL and convert_to == ProgrammingCase.COBOL,
            input_string == ProgrammingCase.CAMEL and convert_to == ProgrammingCase.FLAT,
            input_string == ProgrammingCase.CAMEL and convert_to == ProgrammingCase.KEBAB,
            input_string == ProgrammingCase.CAMEL and convert_to == ProgrammingCase.PASCAL,
            input_string == ProgrammingCase.CAMEL and convert_to == ProgrammingCase.SCREAM,
            input_string == ProgrammingCase.CAMEL and convert_to == ProgrammingCase.SNAKE,

            input_string == ProgrammingCase.COBOL and convert_to == ProgrammingCase.CAMEL,
            input_string == ProgrammingCase.COBOL and convert_to == ProgrammingCase.FLAT,
            input_string == ProgrammingCase.COBOL and convert_to == ProgrammingCase.KEBAB,
            input_string == ProgrammingCase.COBOL and convert_to == ProgrammingCase.PASCAL,
            input_string == ProgrammingCase.COBOL and convert_to == ProgrammingCase.SCREAM,
            input_string == ProgrammingCase.COBOL and convert_to == ProgrammingCase.SNAKE,

            input_string == ProgrammingCase.FLAT and convert_to == ProgrammingCase.CAMEL,
            input_string == ProgrammingCase.FLAT and convert_to == ProgrammingCase.COBOL,
            input_string == ProgrammingCase.FLAT and convert_to == ProgrammingCase.KEBAB,
            input_string == ProgrammingCase.FLAT and convert_to == ProgrammingCase.PASCAL,
            input_string == ProgrammingCase.FLAT and convert_to == ProgrammingCase.SCREAM,
            input_string == ProgrammingCase.FLAT and convert_to == ProgrammingCase.SNAKE,

            input_string == ProgrammingCase.KEBAB and convert_to == ProgrammingCase.CAMEL,
            input_string == ProgrammingCase.KEBAB and convert_to == ProgrammingCase.COBOL,
            input_string == ProgrammingCase.KEBAB and convert_to == ProgrammingCase.FLAT,
            input_string == ProgrammingCase.KEBAB and convert_to == ProgrammingCase.PASCAL,
            input_string == ProgrammingCase.KEBAB and convert_to == ProgrammingCase.SCREAM,
            input_string == ProgrammingCase.KEBAB and convert_to == ProgrammingCase.SNAKE,

            input_string == ProgrammingCase.PASCAL and convert_to == ProgrammingCase.CAMEL,
            input_string == ProgrammingCase.PASCAL and convert_to == ProgrammingCase.COBOL,
            input_string == ProgrammingCase.PASCAL and convert_to == ProgrammingCase.FLAT,
            input_string == ProgrammingCase.PASCAL and convert_to == ProgrammingCase.KEBAB,
            input_string == ProgrammingCase.PASCAL and convert_to == ProgrammingCase.SCREAM,
            input_string == ProgrammingCase.PASCAL and convert_to == ProgrammingCase.SNAKE,

            input_string == ProgrammingCase.SCREAM and convert_to == ProgrammingCase.CAMEL,
            input_string == ProgrammingCase.SCREAM and convert_to == ProgrammingCase.COBOL,
            input_string == ProgrammingCase.SCREAM and convert_to == ProgrammingCase.FLAT,
            input_string == ProgrammingCase.SCREAM and convert_to == ProgrammingCase.KEBAB,
            input_string == ProgrammingCase.SCREAM and convert_to == ProgrammingCase.PASCAL,
            input_string == ProgrammingCase.SCREAM and convert_to == ProgrammingCase.SNAKE,

            input_string == ProgrammingCase.SNAKE and convert_to == ProgrammingCase.CAMEL,
            input_string == ProgrammingCase.SNAKE and convert_to == ProgrammingCase.COBOL,
            input_string == ProgrammingCase.SNAKE and convert_to == ProgrammingCase.FLAT,
            input_string == ProgrammingCase.SNAKE and convert_to == ProgrammingCase.KEBAB,
            input_string == ProgrammingCase.SNAKE and convert_to == ProgrammingCase.PASCAL,
            input_string == ProgrammingCase.SNAKE and convert_to == ProgrammingCase.SCREAM
        ]

        res = [
            wiz.camel_to_cobol(),
            wiz.camel_to_flat(),
            wiz.camel_to_kebab(),
            wiz.camel_to_pascal(),
            wiz.camel_to_scream(),
            wiz.camel_to_snake(),

            wiz.cobol_to_camel(),
            wiz.cobol_to_flat(),
            wiz.cobol_to_kebab(),
            wiz.cobol_to_pascal(),
            wiz.cobol_to_scream(),
            wiz.cobol_to_snake(),

            wiz.flat_to_camel(),
            wiz.flat_to_cobol(),
            wiz.flat_to_kebab(),
            wiz.flat_to_pascal(),
            wiz.flat_to_scream(),
            wiz.flat_to_snake(),

            wiz.kebab_to_camel(),
            wiz.kebab_to_cobol(),
            wiz.kebab_to_flat(),
            wiz.kebab_to_pascal(),
            wiz.kebab_to_scream(),
            wiz.kebab_to_snake(),

            wiz.pascal_to_camel(),
            wiz.pascal_to_cobol(),
            wiz.pascal_to_flat(),
            wiz.pascal_to_kebab(),
            wiz.pascal_to_pascal(),
            wiz.pascal_to_snake(),

            wiz.scream_to_camel(),
            wiz.scream_to_cobol(),
            wiz.scream_to_flat(),
            wiz.scream_to_kebab(),
            wiz.scream_to_pascal(),
            wiz.scream_to_snake(),

            wiz.snake_to_camel(),
            wiz.snake_to_cobol(),
            wiz.snake_to_flat(),
            wiz.snake_to_kebab(),
            wiz.snake_to_pascal(),
            wiz.snake_to_scream(),
        ]

        output_string = np.select(con, res, default=0)

        if not isinstance(output_string, str):
            raise RuntimeError('blah')
        else:
            ic(wiz.input_string)
            ic(wiz.input_case)
            ic(wiz.convert_to)

        return output_string

    def camel_to_cobol(self) -> str:
        return self.input_string    # TODO

    def camel_to_flat(self) -> str:
        return self.input_string    # TODO

    def camel_to_kebab(self) -> str:
        return self.input_string    # TODO

    def camel_to_pascal(self) -> str:
        return self.input_string    # TODO

    def camel_to_scream(self) -> str:
        return self.input_string    # TODO

    def camel_to_snake(self) -> str:
        val = ''
        for char in self.input_string:
            if char.isupper():
                val += '_' + char.lower()
            else:
                val += char
        return val

    def cobol_to_camel(self) -> str:
        return self.input_string    # TODO

    def cobol_to_flat(self) -> str:
        return self.input_string    # TODO

    def cobol_to_kebab(self) -> str:
        return self.input_string    # TODO

    def cobol_to_pascal(self) -> str:
        return self.input_string    # TODO

    def cobol_to_scream(self) -> str:
        return self.input_string    # TODO

    def cobol_to_snake(self) -> str:
        return self.input_string    # TODO

    def flat_to_camel(self) -> str:
        return self.input_string    # TODO

    def flat_to_cobol(self) -> str:
        return self.input_string    # TODO

    def flat_to_kebab(self) -> str:
        return self.input_string    # TODO

    def flat_to_pascal(self) -> str:
        return self.input_string    # TODO

    def flat_to_scream(self) -> str:
        return self.input_string    # TODO

    def flat_to_snake(self) -> str:
        return self.input_string    # TODO

    def kebab_to_camel(self) -> str:
        return self.input_string    # TODO

    def kebab_to_cobol(self) -> str:
        return self.input_string    # TODO

    def kebab_to_flat(self) -> str:
        return self.input_string    # TODO

    def kebab_to_pascal(self) -> str:
        return self.input_string    # TODO

    def kebab_to_scream(self) -> str:
        return self.input_string.upper().replace('-', '_')

    def kebab_to_snake(self) -> str:
        return self.input_string.lower().replace('-', '_')

    def pascal_to_camel(self) -> str:
        return self.input_string    # TODO

    def pascal_to_cobol(self) -> str:
        return self.input_string    # TODO

    def pascal_to_flat(self) -> str:
        return self.input_string    # TODO

    def pascal_to_kebab(self) -> str:
        return self.input_string    # TODO

    def pascal_to_pascal(self) -> str:
        return self.input_string    # TODO

    def pascal_to_snake(self) -> str:
        return self.input_string    # TODO

    def scream_to_camel(self) -> str:
        return self.input_string    # TODO

    def scream_to_cobol(self) -> str:
        return self.input_string    # TODO

    def scream_to_flat(self) -> str:
        return self.input_string    # TODO

    def scream_to_kebab(self) -> str:
        return self.input_string.lower().replace('_', '-')

    def scream_to_pascal(self) -> str:
        return self.input_string.lower().replace('_', ' ').title().replace(' ', '')

    def scream_to_snake(self) -> str:
        return self.input_string.lower()

    def snake_to_camel(self) -> str:
        val = self.input_string.replace('_', ' ').title().replace(' ', '')
        return f'{val[0].lower()}{val[1:]}'

    def snake_to_cobol(self) -> str:
        return self.input_string.upper().replace('_', '-')

    def snake_to_flat(self) -> str:
        return self.input_string.replace('_', '')

    def snake_to_kebab(self) -> str:
        return self.input_string.replace('_', '-')

    def snake_to_pascal(self) -> str:
        return self.input_string.replace('_', ' ').title().replace(' ', '')

    def snake_to_scream(self) -> str:
        return self.input_string.upper()


# ============================================================================ #

if __name__ == '__main__':
    print('\n\n-------------------------- Executing as standalone script...')

    tst_string = 'camelCamelCamel'

    CaseWizard.detect_case()
    CaseWizard.convert()
    CaseWizard.convert_case()

    print(CaseWizard.convert(tst_string, 'camelCase', 'snake_case'))
