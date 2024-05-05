import re
camel_re = r'(?<=.)(?=[A-Z])'
fruits = 'AppleOrangeBananaStrawberryPeach'#Apple Orange Banana Strawberry Peach
print(re.sub(camel_re, ' ', fruits))
