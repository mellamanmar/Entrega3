class Texts:
    def __init__(self, paragraphs, idiom):
        self.paragraphs= paragraphs
        self.idiom= idiom

    def attributes (self):
        print (f"El texto está escrito en {self.idiom} y tiene {self.paragraphs} párrafos")

    def copy (self):
        if self.idiom == "español" or self.idiom == "Español":
            print ("El texto será copiado")
        else:
            print ("Se debe traducir el texto al español")

    def large (self):
        if self.paragraphs < 3:
            print ("El texto no es válido, debe ser más largo")
        elif self.paragraphs > 6:
            print ("Que no exceda de 5 párrafos")
    
        
# text1= Texts (input ("¿De cuántos párrafos es tu texto? "), input("¿En qué idioma esta escrito? "))
# text1.attributes ()
# text1.copy()
# text1.large ()

class BBC (Texts):
    def __init__(self, paragraphs, idiom, type, author):
        super().__init__(paragraphs, idiom)
        self.type= type
        self.author= author

    def who_write (self):
        if self.author != False:
            print (self.author)
        else:
            print ("Ingrese un autor del texto")

    def large (self):
        if self.paragraphs < 10:
            print ("El texto no es válido, debe ser más largo")
        elif self.paragraphs >= 30:
            print ("Que no exceda de 30 párrafos")
        else:
            print ("Listo para publicarse")

    def write (self):
        if self.large == "Listo para publicarse":
            return self.author
    
    def readers (self):
        read= int (input ("¿Cuántas personas han leído el artículo hasta hoy? "))
        print ("El artículo ha sido leído por",read,"personas")            
    
bbc1= BBC (40, "español", "finanzas", "Gilberto Rojas")
bbc1.who_write ()
bbc1.readers ()
bbc1.large ()
bbc1.write ()