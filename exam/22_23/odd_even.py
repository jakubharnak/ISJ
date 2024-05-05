# 1. Write a function that takes a number as an argument and returns 'even' for even numbers and 'odd' for odd numbers.
def e_o(num): return 'eovdedn' [num%2 :: 2]
print(e_o(1))

# Tento kód v Pythonu vypíše řetězec 'odd'.

# Funkce e_o bere jako argument číslo (num) a vrací podřetězec řetězce 'eovdedn'. 
# Podřetězec je určen indexací, která je založena na zbytku po dělení čísla 2 (num%2). 
# Pokud je číslo liché, zbytek po dělení 2 bude 1, takže indexace začne na pozici 1. 
# Druhý parametr indexace ::2 znamená, že se vyberou znaky s krokem 2, tedy každý druhý znak.

# Takže pokud zavoláme e_o(1), dostaneme 'odd', protože začínáme na druhém znaku (index 1) řetězce 'eovdedn' a bereme každý druhý znak.
# Takže dostaneme znaky ‘o’, ‘v’, ‘d’, což tvoří řetězec 'odd'.