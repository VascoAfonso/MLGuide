class Fraction:
    def __init__(self, numerator: int, denominator: int):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_value = gcd(numerator, denominator)

        self._num = numerator // gcd_value
        self._den = denominator // gcd_value
        self._real_value = numerator / denominator

    
    def __str__(self) -> str:
        return str(self._num) + "/" + str(self._den)

    def __repr__(self) -> str:
        return str(self._num) + "/" + str(self._den)
    
    def __add__(self, frac):
        return Fraction(self._num * frac.get_denominator() + frac.get_numerator() * self._den, self._den * frac.get_denominator())
    
    def __mul__(self, frac):
        return Fraction(self._num * frac.get_numerator() , self._den * frac.get_denominators())
    

    def get_numerator(self):
        return self._num
    
    def get_denominator(self):
        return self._den
    
    def get_real_value(self):
        return self._real_value
