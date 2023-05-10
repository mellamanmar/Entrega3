class Animals ():
    def __init__(self, kind, color, WalkFlyDrag, wild_Domestic):
        self.kind= kind
        self.color= color
        self.WalkFlyDrag= WalkFlyDrag
        self.wild_Domestic= wild_Domestic
   
    def attributes(self):
        print(f"El tipo de animal es: {self.kind}\nEs un animal de color {self.color}\nQue {self.WalkFlyDrag} y es {self.wild_Domestic}")
    
    def eat (self):
        print ("El animal esta comiendo")
    
    def run (self):
        if self.WalkFlyDrag == "camina" or self.WalkFlyDrag == "Camina":
            print ("El animal esta corriendo")

animal1= Animals ("mamífero", "amarillo", "camina", "salvaje")
animal1.attributes()
animal1.eat ()
animal1.run ()

class Tiger (Animals):
    def __init__(self, kind, color, WalkFlyDrag, wild_Domestic, name, speed, force, hungry, heat):
        super().__init__(kind, color, WalkFlyDrag, wild_Domestic)
        self.name= name
        self.force= force
        self.hungry= hungry
        self.heat= heat
        self.speed= speed
    
    def attributes (self):
        super().attributes()
        print (f"El animal es un {self.name} tiene {self.force} puntos de fuerza y {self.speed} puntos de velocidad\n¿Tiene hambre? {self.hungry}\n¿Tiene calor? {self.heat}")

    def upload (self, force, speed):
        self.force=self.force+force
        self.speed=self.speed+speed

    def eat (self):
        if self.hungry:
            print ("El animal ha comido")

    def hunt (self,prey):
        hurt= self.speed*self.force
        if hurt > prey.speed:
            print (f"El {self.name} ha cazado a la {prey.name}")
        elif hurt < prey.speed:
            print (f"La/el {prey.name} ha huído")

    def swim (self):
        if self.heat == True:
            print(f"El {self.name} va a nadar")
        else:
            print (f"El {self.name} no tiene calor")
    
tiger1= Tiger ("mamífero", "amarillo y negro", "camina", "salvaje", "Tigre", 10, 2, True, True)
prey= Tiger ("mamífero", "blanco y negro", "camina", "salvaje", "Zebra", 30, 2, False, False)
tiger1.attributes()
prey.attributes()
tiger1.swim()
tiger1.hunt(prey)
tiger1.eat ()
tiger1.upload (10,10)
tiger1.attributes()

class Dog (Animals):
    def __init__(self, kind, color, WalkFlyDrag, wild_Domestic, tenderness, energy):
        super().__init__(kind, color, WalkFlyDrag, wild_Domestic)
        self.tenderness= tenderness
        self.energy= energy

    def attributes (self):
        super().attributes()
        print (f"¿El perro es tierno? {self.tenderness}\nTiene {self.energy} puntos de energía")

    def sleep (self):
        if self.energy < 50:
            print ("El perro necesita dormir")
        elif self.energy > 51:
            print ("El perro quiere jugar")
        else:
            print ("Esa energía no es válida")
    
    def play (self):
        if self.energy > 51:
            person = input("¿Quieres jugar con el perro? ").upper()
            if person == "SI":
                print ("El perro va a jugar contigo")
            elif person == "NO":
                print("No es posible jugar")
        else:
            return self.sleep()
        
    def eat (self):
        print ("El perro esta comiendo")

dog1= Dog ("mamífero", "negro", "camina", "doméstico", True, 60)
dog1.attributes ()
dog1.sleep ()
dog1.eat ()
dog1.play ()