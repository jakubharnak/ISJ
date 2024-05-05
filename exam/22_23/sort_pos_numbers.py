print(sorted([8, 3, 2, 42, 5], key = lambda x: 0 if x == -42 or x == 42 else x))

# sorted() je funkce, která seřadí daný seznam1.
# Parametr key určuje, podle jakého klíče se mají prvky seřadit.
# V tomto případě je klíčem funkce definovaná pomocí lambda, 
# která vrací 0 pro čísla 42 a -42 a pro ostatní čísla vrací jejich hodnotu2.
# Díky tomu se čísla 42 a -42 ocitnou na začátku seřazeného seznamu (protože 0 je menší než ostatní čísla v seznamu),
# zatímco ostatní čísla budou seřazena v vzestupném pořadí3.
# Takže výsledkem tohoto kódu je [42, 2, 3, 5, 8]. <br> 
# Poznámka: Pokud byste chtěli, aby bylo číslo 42 na konci seřazeného seznamu, můžete použít float('inf') 
# místo 0 v lambda funkci. Tím se 42 stane největším číslem a ocitne se na konci seřazeného seznamu.