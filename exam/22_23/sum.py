print(sum(x>5 for x in range(10))) # 4

# range(10) generuje posloupnost čísel od 0 do 9.
# x>5 for x in range(10) je generátorový výraz, který pro každé číslo x v rozsahu vrátí 
# True (což se počítá jako 1), pokud je x větší než 5, a False (což se počítá jako 0) v opačném případě.
# sum() pak sečte všechny hodnoty (1 nebo 0) generované tímto výrazem.
# Takže výsledkem tohoto kódu je počet čísel v rozsahu od 0 do 9, 
# které jsou větší než 5. To je 4 čísla (6, 7, 8 a 9), takže výsledkem je 4