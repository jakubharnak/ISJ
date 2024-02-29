
import re

# ukol za 3 body
def camel_to_snake_case(name):
    """Transfer camelCaseNames to snake_case_names.

    >>> camel_to_snake_case('camelCaseNameAllowed')
    'camel_case_name_allowed'
    >>> camel_to_snake_case('longVATNumber')
    'long_vat_number'
    """

    inbetween = re.compile(r'((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
    return inbetween.sub(r'_\1', name).lower()

# ukol za 2 body
def not_both_titles(names_string):
    """Returns a list of names not preceded by [Pp]rof./[Dd]oc. and 
    followed by ', Ph.D.'

    >>> not_both_titles('doc. Josef Tyl, Rudolf Srp, Ph.D., Pavel Vlk, doc. RNDr. Petr Berka, Ph.D., Jan Hora')
    ['doc. Josef Tyl', 'Rudolf Srp, Ph.D.', 'Pavel Vlk', 'Jan Hora']
    """
    
    pat = re.compile(r'((?:[Pp]rof\.|[Dd]oc\.)\s[\w\s]+(?!,\sPh\.D\.)|(?:[Pp]rof\.|[Dd]oc\.)(?:[\w\s]+(?=,\sPh\.D\.))|[\w\s]+(?!,))')
    return [name for name in pat.findall(names_string) if name]


if __name__ == "__main__":
 import doctest
 doctest.testmod()
