#programa que permita llenar una lista con los numeros primos menores o iguales al numero entero que nos pida el usuario utilice alguna clase con encapsulamiento
#Jose Conejo

class PrimeNumbers:
    def __init__(self):
        self._primes = []

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def generate_primes(self, limit):
        
        self._primes = [num for num in range(2, limit + 1) if self.is_prime(num)]

    def get_primes(self):
    
        return self._primes


def main():
    try:
        limit = int(input("Introduce un número entero: "))
        prime_numbers = PrimeNumbers()
        prime_numbers.generate_primes(limit)
        print(f"Números primos menores o iguales a {limit}: {prime_numbers.get_primes()}")
    except ValueError:
        print("Por favor, introduzca un número entero.")

if __name__ == "__main__":
    main()
