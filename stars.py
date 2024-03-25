import turtle

def draw_star():
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.right(60)
#main
num_stars = int(input("Enter the number of stars: "))
screen = turtle.Screen()
screen.title("Stars")
turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.pendown()
turtle.right(90)
for _ in range(num_stars):
    draw_star()
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
turtle.done()
