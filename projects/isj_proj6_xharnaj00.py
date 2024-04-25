#!/usr/bin/env python3

class Polynomial:
    def __init__(self, *args, **kwargs):
        # If keyword arguments are provided, create a list of coefficients with zeros at corresponding indices.
        # For example, Polynomial(x3=2, x0=1) creates a polynomial with coefficients [1, 0, 0, 2].
        if kwargs:
            self.coeffs = [0]*(max([int(k[1:]) for k in kwargs.keys()])+1)
            for k, v in kwargs.items():
                self.coeffs[int(k[1:])] = v
        else:
            # If the first argument is a list, use it as the coefficients.
            # Otherwise, convert the arguments to a list and use it as the coefficients.
            if isinstance(args[0], list):
                self.coeffs = args[0]
            else:
                self.coeffs = list(args)

    def __str__(self):
        # If all coefficients are zero, return "0".
        if all(coeff == 0 for coeff in self.coeffs):
            return "0"
        # Create a list of terms for the polynomial.
        # Replace "x^0" with "", "x^1" with "x", "1x" with "x", and "-1x" with "-x".
        # Join the terms with " + " and replace "+ -" with "- ".
        terms = ["{}x^{}".format(self.coeffs[i], i) for i in range(len(self.coeffs)) if self.coeffs[i] != 0]
        terms = [term.replace("x^0", "") for term in terms]
        terms = [term.replace("x^1", "x") for term in terms]
        terms = [term.replace("1x", "x") for term in terms]
        terms = [term.replace("-1x", "-x") for term in terms]
        terms = [term.replace("+ -", "- ") for term in terms]
        return " + ".join(reversed(terms)).replace("+ -", "- ")

    def __eq__(self, other):
        # If the polynomials have different degrees, append zeros to the end of the coefficients list.
        # Then compare the coefficients of the polynomials.
        max_length = max(len(self.coeffs), len(other.coeffs))
        self.coeffs += [0]*(max_length - len(self.coeffs))
        other.coeffs += [0]*(max_length - len(other.coeffs))
        return self.coeffs == other.coeffs

    def __add__(self, other):
        # Create a list of result coefficients with zeros at corresponding indices.
        # Add the coefficients of the polynomials to the result coefficients.
        # Return a new Polynomial with the result coefficients.
        max_length = max(len(self.coeffs), len(other.coeffs))
        result_coeffs = [0]*max_length
        for i in range(max_length):
            if i < len(self.coeffs):
                result_coeffs[i] += self.coeffs[i]
            if i < len(other.coeffs):
                result_coeffs[i] += other.coeffs[i]
        return Polynomial(result_coeffs)

    def __mul__(self, other):
        # Create a list of result coefficients with zeros at corresponding indices.
        # Multiply the coefficients of the polynomials and add them to the result coefficients.
        # Return a new Polynomial with the result coefficients.
        result_coeffs = [0]*(len(self.coeffs)+len(other.coeffs)-1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result_coeffs[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial(result_coeffs)

    def __pow__(self, power):
        # Create a new Polynomial with the same coefficients as the original.
        # Multiply the new Polynomial by itself (power-1) times.
        # Return the new Polynomial.
        result = Polynomial(self.coeffs)
        for _ in range(power-1):
            result = result*self
        return result

    def derivative(self):
        # Create a new Polynomial with the derivative of the original.
        # The derivative is computed by multiplying each coefficient by its index.
        return Polynomial([i*self.coeffs[i] for i in range(1, len(self.coeffs))])

    def at_value(self, x, y=None):
        # If only one value is provided, compute the value of the polynomial at x.
        # If two values are provided, compute the difference between the value of the polynomial at y and at x.
        if y is None:
            return sum([self.coeffs[i]*(x**i) for i in range(len(self.coeffs))])
        else:
            return self.at_value(y) - self.at_value(x)


def test():
    assert str(Polynomial(0, 1, 0, -1, 4, -2, 0, 1, 3, 0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5, 1, 0, -1, 4, -2, 0, 1, 3, 0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3=-1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2, 0, 3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1) + Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1, 1, 1, 0]) + Polynomial(1, -1, 1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1, x1=1) ** 1) == "x - 1"
    assert str(Polynomial(x0=-1, x1=1) ** 2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1, x1=1)
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2, x1=3, x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2, 3, 4, -5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5) == 44
    pol5 = Polynomial([1, 0, -2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1, 3.6) == -23.92
    assert pol5.at_value(-1, 3.6) == -23.92

if __name__ == '__main__':
    test()