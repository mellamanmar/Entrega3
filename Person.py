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
    def __init__(self, name, age, profession, career):
        super().__init__(name, age, profession)
        self.career= career
    
    def tellCareer (self):
        print (self.name, "es estudiante en",self.career)

student1=Student (input ("Ingrese su nombre "), input ("su edad "), input ("¿A qué se dedica? "), input ("¿Qué estudia? "))
student1.tellCareer ()