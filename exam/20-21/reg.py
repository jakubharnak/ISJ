import re
camel_re = r'(?<=.)(?=[A-Z])'
fruits = 'AppleOrangeBananaStrawberryPeach'
print(re.sub(camel_re, ' ', fruits))
