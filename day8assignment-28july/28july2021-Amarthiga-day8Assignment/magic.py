#magic variable 
# __add__()
# __str__()
# __new__()
# __init__() --> method of initialization is invoked without any call

#__add__method
n1 =25
print(n1.__add__(5))

name = "Amar"
print(name.__add__(",how are you?"))

#__sub__()
x=32
print(x.__sub__(5))

#__new__ method
class Students:
    def __new__(training):
        print("Students are in the training period")
        inst = object.__new__(training)
        return inst
    def __init__(self):
        print("Hi, everyone!")
        self.name='Sathya'

#__str__()

n=24
print(int.__str__(n))
print(type(n))

#__ge__
class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __ge__(self, x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False
#__repr__ & __name__
class Amarthiga:
      
    def __init__(self, std):             # magic method to initiate object
        self.string = std
    def __repr__(self):
        return 'Object: {}'.format(self.string)      # print our string object
  
# Driver Code
if __name__ == '__main__':
    string1 = Amarthiga('Hello')  # object creation
    print(string1)                # print object location

#magic Operators:
x=6
print(x.__lt__(8))  #__lt__ a<b
print(x.__le__(5))  #__le__ a<=b
print(x.__gt__(12))  #__gt__ a>b
print(x.__ge__(12))  #__ge__ a>=b
print(x.__eq__(6))  #__gt__ a==b
print(x.__ne__(6))  #__gt__ a!=b
print(x.__bool__())  #__bool__ bool(x)
print(x.__hash__())  #__hash__ hash(a)