from typing import Any


class Materials:
    def __init__(self, condition, quantity, take):
        self._condition= condition
        self.quantity= quantity
        self.take= take
    
    def attributes (self):
        print (f"Estamos hablando de {self.quantity} unidades de un material {self._condition}.\n¿Puedes agarrarlo? {self.take} ")
    
    def changesMaterial (self):
        if self._condition == "solido":
            print ("Se fusiona")
        elif self._condition == "liquido":
            print ("Se solidifica")
        elif self._condition == "gaseoso":
            print ("Se condensa")
        elif self._condition == "plasma":
            print ("No hay cambio")
        else:
            print ("Ingrese un estado válido")
    
    def changeQuantity (self, quantity):
        self.quantity= quantity
        print ("Ahora tenemos",self.quantity,"unidades del material")
    
    def takeMaterial (self):
        if self._condition == "solido":
            self.take= True
            print ("Puedes agarrar el material")
        else:
            self.take= False
            print ("No puedes agarrar el material")

    def set_condition (self,condition):
        self._condition= condition
    
    def get_condition (self):
        return self._condition

# material1= Materials ("liquido", 2, "-")
# material1.attributes()
# material1.changesMaterial ()
# material1.changeQuantity (4)
# material1.takeMaterial ()
# material1.get_condition ("líquido")
# material1.attributes ()

class Wood (Materials):
    def __init__(self, condition, quantity, take, type, use, color):
        super().__init__(condition, quantity, take)
        self.type= type
        self.use= use
        self.color= color
    
    def attributes(self):
        print (f"Hay {self.quantity} unidades de madera tipo {self.type},\nde color {self.color}.\nLa vamos a utilizar para {self.use}")

    def changeType (self):
        changeT = input("¿Qué tipo de madera quiere? ").lower()
        self.type= changeT
    
    def changeUse (self):
        changeU= input ("¿Qué quiere hacer con la madera? ").lower()
        self.use= changeU

# wood1= Wood ("solido", 3, True, "cedro", "construcción", "marrón")
# wood1.attributes ()
# wood1.changeType()
# wood1.changeUse ()
# wood1.attributes ()

class Elements (Materials):
    def __init__(self, condition, quantity, take, name, discover, group, discoverTable):
        super().__init__(condition, quantity, take)
        self.name= name
        self.discover= discover
        self.group= group
        self.discoverTable= discoverTable
    
    def how_many_groups (self):
        elementsGroups= int (input ("¿Cuántos grupos hay en la tabla de elementos? "))
        if elementsGroups == 18:
            self.group = elementsGroups
        else:
            print ("¡Respuesta incorrecta!")

    def attributes(self):
        super().attributes()
        print (f"El nombre del elemento es: {self.name} y lo descubrió {self.discover}")
    
    def discovery_table_elements (self):
        discoveryTable= input ("¿Quién descubrió la tabla de los elementos? ")
        if discoveryTable == "Dmitri Mendeleiev":
            self.discoverTable= discoveryTable
        else:
            print ("¡Respuesta incorrecta!")
    
    def newAttributes (self):
        print ("La tabla de elementos tiene",self.group,"y fue descubierta por",self.discoverTable)

element1= Elements ("liquido",2, False, "bromo", "Antoine Balard",0,0)
element1.attributes ()
element1.how_many_groups ()
element1.discovery_table_elements ()
element1.newAttributes ()