'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
#Jose Conejo
#Tarea n1 
class CuentaBancaria:
    def __init__(self, NumeroCuenta=None, NombreCliente=None, FechaApertura=None, SaldoCuenta=0):
        self.__NumeroCuenta = NumeroCuenta
        self.__NombreCliente = NombreCliente
        self.__FechaApertura = FechaApertura
        self.__SaldoCuenta = SaldoCuenta
        
    def get_NumeroCuenta(self):
        return self.__NumeroCuenta

    def get_NombreCliente(self):
        return self.__NombreCliente

    def get_FechaApertura(self):
        return self.__FechaApertura

    def get_SaldoCuenta(self):
        return self.__SaldoCuenta

    def set_NumeroCuenta(self, NumeroCuenta):
        self.__NumeroCuenta = NumeroCuenta

    def set_NombreCliente(self, NombreCliente):
        self.__NombreCliente = NombreCliente

    def set_FechaApertura(self, FechaApertura):
        self.__FechaApertura = FechaApertura

    def set_SaldoCuenta(self, SaldoCuenta):
        if SaldoCuenta >= 100000:
            self.__SaldoCuenta = SaldoCuenta
        else:
            print("El saldo inicial mínimo debe ser de $100.000 pesos")
            
    def AbrirCuenta(self, NumeroCuenta, NombreCliente, FechaApertura, SaldoCuenta):
        if SaldoCuenta >= 100000:
            self.set_NumeroCuenta(NumeroCuenta)
            self.set_NombreCliente(NombreCliente)
            self.set_FechaApertura(FechaApertura)
            self.set_SaldoCuenta(SaldoCuenta)
            print("Su cuenta ha sido abierta correctamente.")
        else:
            print("No se pudo abrir la cuenta. El saldo inicial no es suficiente.")
            
    def Consignar(self, valor):
        if valor > 0:
            self.__SaldoCuenta += valor
            print(f"Consignación exitosa. Nuevo saldo: {self.__SaldoCuenta}")
        else:
            print("La consignación debe ser un valor positivo.")
            
    def Retirar(self, valor):
        if 0 < valor <= self.__SaldoCuenta:
            self.__SaldoCuenta -= valor
            print(f"Su retiro ha sido exitoso. Nuevo saldo: {self.__SaldoCuenta}")
        else:
            print("No se puede realizar el retiro. Verifique el valor indicado e intente de nuevo.")        

def menu():
    cuenta = CuentaBancaria()

    while True:
        print("\n--- Menú de operaciones bancarias ---")
        print("1. Abrir cuenta")
        print("2. Consultar saldo")
        print("3. Consignar")
        print("4. Retirar")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            NumeroCuenta = input("Ingrese el número de cuenta: ")
            NombreCliente = input("Ingrese el nombre del cliente: ")
            FechaApertura = input("Ingrese la fecha de apertura (dd/mm/aaaa): ")
            SaldoCuenta = float(input("Ingrese el saldo inicial: "))
            cuenta.AbrirCuenta(NumeroCuenta, NombreCliente, FechaApertura, SaldoCuenta)

        elif opcion == "2":
            print(f"Saldo actual: {cuenta.get_SaldoCuenta()}")

        elif opcion == "3":
            valor = float(input("Ingrese el valor a consignar: "))
            cuenta.Consignar(valor)

        elif opcion == "4":
            valor = float(input("Ingrese el valor a retirar: "))
            cuenta.Retirar(valor)

        elif opcion == "5":
            print("Gracias por utilizar el servicio bancario.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

menu()
  
