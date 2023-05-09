class Person ():

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def greet (self):
        print (self.name, "te saluda")
    
    def present (self):
        print ("Hola, mi nombre es ", self.name, "mi edad es ", self.age, " y soy ", self.profession)

person1= Person (input ("Ingrese su nombre "), input ("su edad "), input ("¿A qué se dedica? "))
person1.greet ()
person1.present ()

class Student(Person):
    def __init__(self, name, age, profession, career, energy, knowledge):
        super().__init__(name, age, profession)
        self.career= career
        self.energy= energy
        self.knowledge= knowledge
    
    def tellCareer (self):
        print (self.name,"es estudiante en",self.career)
    
    def goToClass (self, energy):
        self.energy=energy
        if self.energy > 0:
            print (self.name,"debe ir a clases")
        else:
            print (self.name,"debe dormir")

    def homework (self):
        if self.energy and self.knowledge > 0:
            print (self.name,"va a hacer la tarea")
        else:
            print (self.name,"debe estudiar más")
            

    def greet (self):
        print (self.name, "te saluda")

student1=Student ("Clara",22, "Estudiante", "Medicina", 100, 20)
student1.tellCareer ()
student1.greet ()
student1.homework ()
student1.goToClass (100)


