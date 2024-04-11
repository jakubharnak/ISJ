def find_common_elements(str1, str2):
  """
  Najde společné prvky v zadaných řetězcích.

  Argumenty:
    str1 (str): První řetězec s hodnotami oddělenými středníkem.
    str2 (str): Druhý řetězec s hodnotami oddělenými znakem "zavináč".

  Vrací:
    set: Množina obsahující společné prvky.
  """

  # Rozdělení řetězců na seznam hodnot
  values1 = str1.split(';')
  values2 = str2.split('@')

  # Převod seznamů na množiny
  set1 = set(values1)
  set2 = set(values2)

  # Společné prvky
  used_by_both = set1 & set2

  return used_by_both

# Testování funkce
teststr1 = 'Ada;Bob;Bob;Ada;Cyril;Ada;Cyril'
teststr2 = 'Dan@Ada@Ada@Dan@Cyril@Ed@Frank'

for ev in find_common_elements(teststr1, teststr2):
  print(ev)
