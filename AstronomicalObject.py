class AstronomicalObject ():
    def __init__(self, name, size, color, shine):
        self.name = name
        self.size = size
        self.color = color
        self.shine = shine
    
    def solarSistem (self):
        if self.name == "venus" or self.name == "mercurio" or self.name == "tierra" or self.name == "marte" or self.name == "jupiter" or self.name == "saturno" or self.name == "urano" or self.name == "neptuno":
            print ("Es un planeta del sistema solar")
        else:
            print ("No es un planeta del sistema solar")
    
    def tipe (self):
        if self.name == "venus" or self.name == "tierra" or self.name == "mercurio" or self.name == "marte":
            print ("Es un planeta rocoso")
        if self.name == "jupiter" or self.name == "saturno" or self.name == "urano" or self.name == "neptuno":
            print ("Es un planeta gaseoso")
    
    def planetColor (self):
        if self.color == "gris":
            print ("El planeta gris del sistema solar es Mercurio")
        elif self.color == "marron" or self.color == "marrón":
            print ("Los planetas marrones del sistema solar son Venus y Júpiter")
        elif self.color == "rojo":
            print ("El planeta rojo del sistema solar es Marte")
        elif self.color == "dorado":
            print ("El planeta dorado del sistema solar es Saturno")
        elif self.color == "azul":
            print ("Los planetas azules del sistema solar son Urano, Tierra y Mercurio")
        else:
            print ("No es un planeta del sistema solar")
    
    def brightness (self):
        if self.shine == "si":
            print ("Puede ser una estrella")
        else:
            print ("Es un planeta")


cuerpo1 = AstronomicalObject ("Venus", "Pequeño", "marron", "no") .lower()
cuerpo1.color
cuerpo1.planetColor()
cuerpo1.tipe ()
cuerpo1.brightness ()
cuerpo1.solarSistem ()


class Star(AstronomicalObject):
    def __init__(self, name, size, color, shine, discovery):
        super().__init__(name, size, color, shine)
        self.discovery= discovery

    def starDiscovery (self):
        print ("La estrella fue descubierta en ",self.discovery)

star1=Star ("Rigel", "", "azul", True, "1603")
star1.starDiscovery ()