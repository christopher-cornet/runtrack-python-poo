class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        print('Le nombre1 est', self.nombre1)
        print('Le nombre2 est', self.nombre2)

    def addition(self, nombre1, nombre2):
        result = nombre1 + nombre2
        print('Le résultat est', result)
         
Operation(5, 10)
Operation.addition(Operation, 5, 10)