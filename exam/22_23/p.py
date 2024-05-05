import re
#print(re.sub(r'cat', 'dog', 'A Cat', re.IGNORECASE)) wrong
print(re.sub(r'cat', 'dog', 'A Cat', flags=re.IGNORECASE)) #fixed

# Tento kód vypíše A dog, protože re.IGNORECASE způsobí, že regulární výraz bude ignorovat velikost písmen.
# Takže cat odpovídá jak Cat, tak cat. 
# A re.sub nahradí všechny výskyty cat (bez ohledu na velikost písmen) řetězcem dog.