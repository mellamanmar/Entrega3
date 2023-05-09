class Drinks:

    def __init__(self, name, tipe, quantity):
        self.name = name
        self.tipe = tipe
        self.quantity = quantity
    
    def atributos (self):
        print (f"Tenemos {self.quantity} de {self.name} que es una bebida de tipo {self.tipe}")
    
    def drinkUp (self):
        if self.tipe == "alcohólica" or self.tipe == "alcoholica":
            age= input ("¿Eres mayor de edad? ").upper()
            if age == "SI":
                print ("Te tomas la/el",self.name)
            elif age == "NO":
                print ("Debes ser mayor de edad")
            else:
                print ("Ingrese una respuesta válida")
        elif self.tipe == "jugo" or self.tipe == "refresco" or self.tipe == "agua":
            print ("Te tomas la/el",self.name)
        else:
            print ("El tipo de bebida no es válido")

    def changeDrink (self, name):
        self.name = name
        print ("Ahora tu bebida es ",self.name)

tequila=Drinks ("Tequila", "alcoholica", "1 copa")
tequila.atributos ()
tequila.drinkUp ()
tequila.changeDrink ("vodka")

class StrawberryJuice (Drinks):
    def __init__(self, name, tipe, quantity, sugary):
        super().__init__(name, tipe, quantity)
        self.sugary= sugary
    
    def atributos(self):
        super().atributos()
        print ("y tiene un",self.sugary,"por ciento de azúcar")
    
    def changeDrink(self, name):
        return super().changeDrink(name)
    

strawberry1= StrawberryJuice ("Jugo de fresa", "jugo", "1 vaso", 20)
strawberry1.atributos ()
strawberry1.changeDrink ("parchita")
strawberry1.atributos ()