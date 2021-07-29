class Amar:
    __name ="Yazhini"  #hidden
    def test(self):
        print(__name)
objA =Amar()
#print(objA.test()) 
#print(objA.__name) #error

print(objA._Amar__name)   # syntax print(object._classname__hidden variable name)
