class Operaciones:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1+self.num2
    def resta(self):
        return self.num1-self.num2

#instanciamos

Op = Operaciones(5,4)
print (Op.suma())
print (Op.resta())
