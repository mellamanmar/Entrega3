class Texts:
    def __init__(self, large, idiom):
        self.large= large
        self.idiom= idiom
    
    def copy (self):
        if self.idiom == "español" or self.idiom == "Español":
            print ("El texto será copiado")
        else:
            print ("Se debe traducir el texto al español")

    def change (self):
        if self.large < 3:
            print ("El texto no es válido, debe ser más largo")
        if self.large > 20:
            print ("Que no exceda de 5 párrafos")
        
text1= Texts (input ("¿De cuántos párrafos es tu cuento? "), input("¿En qué idioma esta escrito? "))
text1.copy()

class StoryTale(Texts):
    def __init__(self, large, idiom, type):
        super().__init__(large, idiom)
        self.type= type
    
    def whatKind (self):
        print (f"Te vamos a leer una historia de {self.type} en {self.idiom}")
        return self.type

story1= StoryTale (3, "español", "terror")
story1.whatKind()