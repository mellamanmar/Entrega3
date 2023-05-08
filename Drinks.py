class Drinks:

    def __init__(self, name, flavor, color, origin, tipe):
        self.name = name
        self.flavor = flavor
        self.color = color
        self.origin = origin
        self.tipe = tipe
    
    def OriginDrink (self):
        print ("El ", self.name, "es de ", self.origin)
    
    def FlavorDrink (self):
        if self.flavor == "dulce":
            print ("La bebida es dulce")
        if self.flavor == "acido":
            print ("La bebida es ácida")
        if self.flavor == "amarga":
            print ("La bebida es amarga")
        if self.flavor == "picante":
            print ("La bebida es picante")
    
    def changeDrink (self, newFlavor):
        self.flavor = newFlavor
        print ("Ahora tu bebida es ", newFlavor)

tequila=Drinks ("margarita", "picante", "transparente", "México", "alcohólica")
tequila.OriginDrink()

class Fruit(Drinks):
    def __init__(self, name, flavor, color, origin, tipe, season):
        super().__init__(name, flavor, color, origin, tipe)
        self.season= season
    
    def seasonFruit (self):
        print ("El",self.name, "se da más en",self.season)

fresa= Fruit("jugo de fresa", "dulce", "rojo", "tropical", "frutal", "primavera")
fresa.seasonFruit ()