#1
import turtle as t

"canvas, which is the area inside the window on whichwe can draw"
sn = t.Screen()
sn.bgcolor("yellow")
sn.title("Hello,Amar!!")

amar = t.Turtle()
amar.color("red")
amar.pensize(4)

amar.circle(25)

sn.mainloop()


#2
import random

print(random.random())
print(random.randint(4,35))
print(random.randrange(11,20,10))

print(random.choice("AmarthigaK"))
print(random.choice((12,33,45,67,78)))
print(random.choice(("amar","div","kowsi")))

n=[12,23,45,67,65,43]
print(random.shuffle(n))


#3
import cProfile
#4
import re
cProfile.run('re.compile("foo|bar")')

cProfile.run('re.compile("foo|bar")', 'restats')

#5
import sysconfig
sysconfig.get_config_var('Py_ENABLE_SHARED')
