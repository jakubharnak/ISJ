import re
text = 'abbacccdee'

result = [m[0] for m in re.finditer(
                                    r'(.)\1*' # group of the same characters 
                                    , text)]
print(result)

# Tento regulární výraz (.)\1* funguje tak, že (.) odpovídá jakémukoli znaku a \1* odpovídá nula nebo více opakování stejného znaku. 