#1
class A:
    def sayHello(self):
        print("Hello")

class B(A):
    def sayHello(self):
        print("Hai")

obja = A()
objb = B()

obja.sayHello()
objb.sayHello()

#2
def add(a,b,c=0):
    return a+b-c
print(add(4,5))
print(add(3,6,7))

