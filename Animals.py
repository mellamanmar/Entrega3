class Animals ():
    def __init__(self, kind, color, name, wild_Domestic):
        self.kind= kind
        self.color= color
        self.name= name
        self.wild_Domestic= wild_Domestic

    def move (self):
        if self.kind == "terrestre":
            print ("El animal camina")
        elif self.kind == "volador":
            print ("El animal vuela")
        elif self.kind == "rastrero":
            print ("El animal se arrastra")
        else:
            print ("No tenemos ese tipo en nuestro sistema")
    
    def wildOrDomestic (self):
        if self.wild_Domestic == "salvaje":
            print ("El animal es salvaje")
        if self.wild_Domestic == "domestico" or self.wild_Domestic == "doméstico":
            print ("El animal es doméstico")

    def talk (self):
        if self.name == "loro":
            print ("Sí habla")
        else:
            print ("No habla")

animal1= Animals (input ("¿El animal es terrestre, volador o rastrero? ") .lower(), input("¿De qué color es el animal? ") .lower(), input ("¿Qué animal es? ") .lower(), input ("¿Es salvaje o doméstico? ") .lower())
animal1.move ()
animal1.talk ()
animal1.wildOrDomestic ()

class Felines(Animals):
    def __init__(self, kind, color, name, wild_Domestic, country):
        super().__init__(kind, color, name, wild_Domestic)
        self.country= country
    
    def whatCountry (self):
        print ("El ",self.name, "es de ",self.country)

gatoMontes= Felines ("Terrestre", "marrón", "Gato Monntés", "Salvaje", "Europa, Asia y África")
gatoMontes.whatCountry ()