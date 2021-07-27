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
