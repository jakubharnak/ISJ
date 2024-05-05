slovnik = {(1,'b','C'): [1,2], (2,'A','c'): [2,3], (3,'c','d'): [0,0,0], (4,'e','b'): [2,3], (2,'a','b'): [2,3]}
serazeny_slovnik = sorted(slovnik.items(), key=lambda item: (len(item[1]), -ord(item[0][2].lower()), -ord(item[0][1].lower())))

# Výpis seřazeného slovníku na jednom řádku
print(','.join(map(str, serazeny_slovnik)))

#((1, 'b', 'C'), [1, 2]),((2, 'A', 'c'), [2, 3]),((4, 'e', 'b'), [2, 3]),((2, 'a', 'b'), [2, 3]),((3, 'c', 'd'), [0, 0, 0])