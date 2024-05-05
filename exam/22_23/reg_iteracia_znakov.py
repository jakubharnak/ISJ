import re
text = 'abbacccdee'

result = [m[0] for m in re.finditer(r'(a+|b+|c+|d+)', text)] # or r'(.)\1*'
print(result)

# Tento regulární výraz (.)\1* funguje tak, že (.) odpovídá jakémukoli znaku a \1* odpovídá nula nebo více opakování stejného znaku. 