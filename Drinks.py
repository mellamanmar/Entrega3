class Drinks:

    def __init__(self, name, tipe, quantity):
        self._name = name
        self.tipe = tipe
        self.quantity = quantity
    
    def atributos (self):
        print (f"Tenemos {self.quantity} de {self._name} que es una bebida de tipo {self.tipe}")
    
    def drinkUp (self):
        if self.tipe == "alcohólica" or self.tipe == "alcoholica":
            age= input ("¿Eres mayor de edad? ").upper()
            if age == "SI":
                print ("Te tomas la/el",self._name)
            elif age == "NO":
                print ("Debes ser mayor de edad")
            else:
                print ("Ingrese una respuesta válida")
        elif self.tipe == "jugo" or self.tipe == "refresco" or self.tipe == "agua":
            print ("Te tomas la/el",self._name)
        else:
            print ("El tipo de bebida no es válido")

    def set_name (self, name):
        self._name = name
    
    def get_name (self):
        return self._name

tequila=Drinks ("Tequila", "alcoholica", "1 copa")
tequila.atributos ()
tequila.drinkUp ()
tequila.set_name ("vodka")
print ("Se cambia la bebida por",tequila.get_name())
tequila.atributos ()

class StrawberryJuice (Drinks):
    def __init__(self, name, tipe, quantity, sugary):
        super().__init__(name, tipe, quantity)
        self.sugary= sugary
    
    def atributos(self):
        super().atributos()
        print ("y tiene un",self.sugary,"por ciento de azúcar")
    
    def set_name(self, name):
        return super().set_name(name)
    
    def get_name(self):
        return super().get_name()
    
    def sell (self, price):
        self.price= price
        if self.price > 0:
            print (f"El {self._name} se venderá en {self.price}")
        else:
            print ("Ingrese un precio válido")

strawberry1= StrawberryJuice ("Jugo de fresa", "jugo", "1 vaso", 20)
strawberry1.atributos ()
strawberry1.set_name ("parchita")
strawberry1.atributos ()
strawberry1.sell (int(input ("¿Cuál es el precio de la bebida? ")))