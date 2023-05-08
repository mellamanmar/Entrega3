class Materials:
    def __init__(self, color, name, weighty=False):
        self.color= color
        self.name= name
        self.weighty= weighty
    
    def takeMaterial (self):
        if self.weighty == False:
            print (f"Toma el/la {self.name}")
        else:
            print (f"No es posible tomar el/la {self.name}")

material1= Materials ("Verde", "Esmeralda")
material1.takeMaterial()

class House(Materials):
    def __init__(self, color, name, weighty,use,place):
        super().__init__(color, name, weighty)
        self.use=use
        self.place= place
    
    def MaterialKitchen (self):
        if self.place=="cocina" or self.place=="Cocina":
            print (f"La {self.name} está en {self.place}, ¿puedes moverlo?")

house1= House ("Negro", "Licuadora", False, "Licuar", "Cocina")
house1.MaterialKitchen()
