import re

class RegexFullMatch(str):
    def __eq__(self, other):
        return bool(re.fullmatch(other, self))

print(RegexFullMatch('hello') == 'h.*o')

# Tato třída dědí od třídy str, takže může být použita jako řetězec. 
# Metoda __eq__ je speciální metoda, která se volá, když se používá operátor rovnosti (==). 
# V této metodě používáme funkci re.fullmatch, která zkontroluje, zda celý řetězec odpovídá danému regulárnímu výrazu.

# Takže například RegexFullMatch('hello') == 'h.*o' vrátí True, 
# protože řetězec “hello” odpovídá vzoru “h.*o” 
# (kde . znamená jakýkoli znak a * znamená nula nebo více opakování předchozího znaku).