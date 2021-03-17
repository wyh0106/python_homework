import turtle
# 蓝环
turtle.penup()
turtle.goto(-185, 0)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('blue')
turtle.circle(75)
# 黄环
turtle.penup()
turtle.goto(-92.5, -72.5)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('yellow')
turtle.circle(75)
# 黑环
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('black')
turtle.circle(75)
# 绿环
turtle.penup()
turtle.goto(92.5, -72.5)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('green')
turtle.circle(75)
# 红环
turtle.penup()
turtle.goto(185, 0)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('red')
turtle.circle(75)

turtle.exitonclick()
# print(turtle.position(), turtle.heading())
