class Polynomial:
    def __init__(self, polynom):
        self.polynom = polynom

    def derivate(self):
        derivate = []
        for i in range(1, len(self.polynom)):
            derivate.append(i * self.polynom[i])
        return derivate

# Testovací polynom: 2x^3 + 3x + 1
p = Polynomial([1, 3, 0, 2])
# Výpis derivace
print("Derivace:", p.derivate())
